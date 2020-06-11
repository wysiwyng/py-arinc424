from collections import defaultdict
from functools import partial

record_defs = {
    ('P', 'A') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'designator' : (14, 3),
        'res1' : (17, 2),
        'cont_rec' : (22, 1),
        'spd_limit_alt' : (23, 5),
        'longest_rwy' : (28, 3),
        'ifr_cap' : (31, 1),
        'longest_rwy_surf' : (32, 1),
        'ref_lat' : (33, 9),
        'ref_lon' : (42, 10),
        'mag_var' : (52, 5),
        'arpt_elev' : (57, 5),
        'spd_limit' : (62, 3),
        'rcmd_navaid' : (65, 4),
        'icao_code2' : (69, 2),
        'trns_alt' : (71, 5),
        'trns_lvl' : (76, 5),
        'pub_mil' : (81, 1),
        'tz' : (82, 3),
        'dst' : (85, 1),
        'mag_true' : (86, 1),
        'datum_code' : (87, 3),
        'res2' : (90, 4),
        'arpt_name' : (94, 30)
    },
    ('P', 'B') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'gate_ident' : (14, 5),
        'cont_rec' : (22, 1),
        'gate_lat' : (33, 9),
        'gate_lon' : (42, 10),
        'res1' : (52, 47),
        'gate_name' : (99, 25)
    },
    ('P', 'C') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'wpt_ident' : (14, 5),
        'icao_code2' : (20, 2),
        'cont_rec' : (22, 1),
        'wpt_type' : (27, 3),
        'wpt_use' : (30, 2),
        'wpt_lat' : (33, 9),
        'wpt_lon' : (42, 10),
        'dyn_mag_var' : (75, 5),
        'dat_code' : (85, 3),
        'res1' : (88, 8),
        'nfi' : (96, 3),
        'wpt_name' : (99, 25)
    },
    ('P', 'D') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'sid_ident' : (14, 6),
        'rte_type' : (20, 1),
        'trans_ident' : (21, 5),
        'seq_num' : (27, 3),
        'fix_ident' : (30, 5),
        'icao_code2' : (35, 2),
        'cont_rec' : (39, 1),
        'wpt_desc_code' : (40, 4),
        'turn_dir' : (44, 1),
        'rcmd_navaid' : (51, 4),
        'icao_code3' : (55, 2),
        'arc_radius' : (57, 6),
        'theta' : (63, 4),
        'rho' : (67, 4),
        'mag_crs' : (71, 4),
        'rt_hold' : (75, 4),
        'recd_nav_sec' : (79, 1),
        'recd_nav_sub' : (80, 1),
        'res1' : (81, 2),
        'alt_desc' : (83, 1),
        'atc_ind' : (84, 1),
        'alt1' : (85, 5),
        'alt2' : (90, 4),
        'trans_alt' : (95, 5),
        'spd_lim' : (100, 3),
        'v_ang' : (103, 4),
        'cfix' : (107, 5),
        'mcode' : (112, 1),
        'icao_code4' : (113, 2),
        'sec_code' : (115, 1),
        'sub_code' : (116, 1),
        'gps_ind' : (117, 1),
        'spd_lim_desc' : (118, 1),
        'apch_rte_q1' : (119, 1),
        'apch_rte_q2' : (120, 1)
    },
    ('P', 'E') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'star_ident' : (14, 6),
        'rte_type' : (20, 1),
        'trans_ident' : (21, 5),
        'seq_num' : (27, 3),
        'fix_ident' : (30, 5),
        'icao_code2' : (35, 2),
        'cont_rec' : (39, 1),
        'wpt_desc_code' : (40, 4),
        'turn_dir' : (44, 1),
        'rcmd_navaid' : (51, 4),
        'icao_code3' : (55, 2),
        'arc_radius' : (57, 6),
        'theta' : (63, 4),
        'rho' : (67, 4),
        'mag_crs' : (71, 4),
        'rt_hold' : (75, 4),
        'recd_nav_sec' : (79, 1),
        'recd_nav_sub' : (80, 1),
        'res1' : (81, 2),
        'alt_desc' : (83, 1),
        'atc_ind' : (84, 1),
        'alt1' : (85, 5),
        'alt2' : (90, 4),
        'trans_alt' : (95, 5),
        'spd_lim' : (100, 3),
        'v_ang' : (103, 4),
        'cfix' : (107, 5),
        'mcode' : (112, 1),
        'icao_code4' : (113, 2),
        'sec_code' : (115, 1),
        'sub_code' : (116, 1),
        'gps_ind' : (117, 1),
        'spd_lim_desc' : (118, 1),
        'apch_rte_q1' : (119, 1),
        'apch_rte_q2' : (120, 1)
    },
    ('P', 'F') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'appr_ident' : (14, 6),
        'rte_type' : (20, 1),
        'trans_ident' : (21, 5),
        'seq_num' : (27, 3),
        'fix_ident' : (30, 5),
        'icao_code2' : (35, 2),
        'cont_rec' : (39, 1),
        'wpt_desc_code' : (40, 4),
        'turn_dir' : (44, 1),
        'rcmd_navaid' : (51, 4),
        'icao_code3' : (55, 2),
        'arc_radius' : (57, 6),
        'theta' : (63, 4),
        'rho' : (67, 4),
        'mag_crs' : (71, 4),
        'rt_hold' : (75, 4),
        'recd_nav_sec' : (79, 1),
        'recd_nav_sub' : (80, 1),
        'res1' : (81, 2),
        'alt_desc' : (83, 1),
        'atc_ind' : (84, 1),
        'alt1' : (85, 5),
        'alt2' : (90, 4),
        'trans_alt' : (95, 5),
        'spd_lim' : (100, 3),
        'v_ang' : (103, 4),
        'cfix' : (107, 5),
        'mcode' : (112, 1),
        'icao_code4' : (113, 2),
        'sec_code' : (115, 1),
        'sub_code' : (116, 1),
        'gps_ind' : (117, 1),
        'spd_lim_desc' : (118, 1),
        'apch_rte_q1' : (119, 1),
        'apch_rte_q2' : (120, 1)
    },
    ('P', 'G') : {
        'icao_ident' : (7, 4),
        'icao_code' : (11, 2),
        'rwy_ident' : (14, 5),
        'cont_rec' : (22, 1),
        'rwy_len' : (23, 5),
        'rwy_brg' : (28, 4),
        'rwy_lat' : (33, 9),
        'rwy_lon' : (42, 10),
        'rwy_grad' : (52, 5),
        'thrs_ele' : (67, 5),
        'thrs_dist' : (72, 4),
        'thrs_crs_h' : (76, 2),
        'rwy_width' : (78, 3),
        'tch' : (81, 1),
        'ref_path1_id' : (82, 4),
        'ref_path1_cat' : (86, 1),
        'stpwy' : (87, 4),
        'ref_path2_id' : (91, 4),
        'ref_path2_cat' : (95, 1),
        'res1' : (96, 6),
        'rwy_desc' : (102, 22)
    }
}

p_to_name = {
    'C': 'wpts',
    'D': 'sids',
    'E': 'stars',
    'F': 'apprs',
    'G': 'rwys',
    'I': 'loc_gls',
    'P': 'pp',
    'S': 'msas'
}

def read_record(sec, sub, line):
    record = None
    if (sec, sub) in record_defs:
        record = {}
        for field_name, (field_begin, field_len) in record_defs[(sec, sub)].items():
            record[field_name] = line[field_begin - 1:field_begin + field_len - 1].strip()
    return record

records = defaultdict(list)

airports = {}

with open('FAACIFP18', 'r') as inf:
    for line in inf:
        if line.startswith('HDR'):
            continue
        record_type = line[0]
        region_code = line[1:4]
        section_code = line[4]

        if section_code == 'U':
            continue

        sub_code = (line[5] + line[12]).strip()

        rec = read_record(section_code, sub_code, line)

        if rec:
            records[section_code + sub_code].append(rec)

            if section_code == 'P':
                arpt_id = rec['icao_ident']

                if sub_code == 'A':
                    airports[arpt_id] = rec
                    airports[arpt_id]['wpts'] = {}
                    airports[arpt_id]['sids'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                    airports[arpt_id]['stars'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                    airports[arpt_id]['apprs'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                    airports[arpt_id]['rwys'] = {}
                    airports[arpt_id]['loc_gs'] = []
                    airports[arpt_id]['pp'] = []
                    airports[arpt_id]['msas'] = []
                elif sub_code == 'C':
                    airports[arpt_id]['wpts'][rec['wpt_ident']] = rec
                elif sub_code == 'D':
                    airports[arpt_id]['sids'][rec['sid_ident']][rec['rte_type']][rec['trans_ident']].append(rec)
                elif sub_code == 'E':
                    airports[arpt_id]['stars'][rec['star_ident']][rec['rte_type']][rec['trans_ident']].append(rec)
                elif sub_code == 'F':
                    airports[arpt_id]['apprs'][rec['appr_ident']][rec['rte_type']][rec['trans_ident']].append(rec)
                elif sub_code == 'G':
                    airports[arpt_id]['rwys'][rec['rwy_ident']] = rec



#for sec, items in records.items():
#    for it in items:
#        if it.get('cont_rec') != '0':
#            print(f'continued record, sec {sec}')

pass