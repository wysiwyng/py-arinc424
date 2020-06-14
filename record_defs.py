empty_record = {}

wpt_record_pri = {
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
	}

apt_record_pri = {
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
	}

apt_gate_record_pri = {
		'icao_ident' : (7, 4),
		'icao_code' : (11, 2),
		'gate_ident' : (14, 5),
		'cont_rec' : (22, 1),
		'gate_lat' : (33, 9),
		'gate_lon' : (42, 10),
		'res1' : (52, 47),
		'gate_name' : (99, 25)
	}

apt_proc_record_pri = {
		'icao_ident' : (7, 4),
		'icao_code' : (11, 2),
		'proc_ident' : (14, 6),
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
	}

apt_rwy_record_pri = {
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

record_map = {
	('A', 'S') : empty_record,						# MORA
	('D', '')  : empty_record,						# VHF Navaid
	('D', 'B') : empty_record,						# NDB Navaid
	
	('E', 'A') : wpt_record_pri,
	('E', 'M') : empty_record,						# Airway Markers
	('E', 'P') : empty_record,						# Holding Patterns
	('E', 'R') : empty_record,						# Airways / Routes
	('E', 'T') : empty_record,						# Preferred Routes
	('E', 'U') : empty_record,						# Airway Restrictions
	('E', 'V') : empty_record,						# Communications

	('H', 'A') : empty_record,						# Heliport Pads
	('H', 'C') : wpt_record_pri,					# Heliport Wpts
	('H', 'D') : apt_proc_record_pri,				# Heliport SIDs
	('H', 'E') : apt_proc_record_pri,				# Heliport STARs
	('H', 'F') : apt_proc_record_pri,				# Heliport Appch
	('H', 'K') : empty_record,						# Heliport TAA
	('H', 'S') : empty_record,						# Heliport MSA
	('H', 'V') : empty_record,						# Heliport Comms

	('P', 'A') : apt_record_pri,
	('P', 'B') : apt_gate_record_pri,
	('P', 'C') : wpt_record_pri,
	('P', 'D') : apt_proc_record_pri,
	('P', 'E') : apt_proc_record_pri,
	('P', 'F') : apt_proc_record_pri,
	('P', 'G') : apt_rwy_record_pri,
	('P', 'I') : empty_record,						# Loc / GS
	('P', 'K') : empty_record,						# TAA
	('P', 'L') : empty_record,						# MLS
	('P', 'M') : empty_record,						# Loc Marker
	('P', 'N') : empty_record,						# Terminal NDB
	('P', 'P') : empty_record,						# Path Point
	('P', 'R') : empty_record,						# Flt Planning ARR/DEP
	('P', 'S') : empty_record,						# MSA
	('P', 'T') : empty_record,						# GLS Station
	('P', 'V') : empty_record,						# Comms

	('R', '') : empty_record,
	('R', 'A') : empty_record,

	('T', 'C') : empty_record,
	('T', 'G') : empty_record,

	('U', 'C') : empty_record,
	('U', 'F') : empty_record,
	('U', 'R') : empty_record,
}