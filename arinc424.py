from collections import defaultdict
from functools import partial
from tqdm import tqdm
import sys
import os

from record_defs import record_map

def read_record(sec, sub, line):
    record = None
    if (sec, sub) in record_map:
        record = {}
        for field_name, (field_begin, field_len) in record_map[(sec, sub)].items():
            record[field_name] = line[field_begin - 1:field_begin + field_len - 1].strip()
    return record

records = defaultdict(list)

airports = {}
waypoints = {}

fname = sys.argv[1]
fsize = os.path.getsize(fname)
num_lines = fsize / (132 + 2)

with open(fname, 'r') as inf:
    for line in tqdm(inf, total=num_lines):
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
            if 0:
                if section_code == 'E':
                    if sub_code == 'A':
                        waypoints[rec['wpt_ident']] = rec

                elif section_code == 'P':
                    arpt_id = rec['icao_ident']

                    if sub_code == 'A':
                        airports[arpt_id] = rec
                        airports[arpt_id]['sids'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                        airports[arpt_id]['stars'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                        airports[arpt_id]['apprs'] = defaultdict(partial(defaultdict, partial(defaultdict, list)))
                        airports[arpt_id]['rwys'] = {}
                        airports[arpt_id]['loc_gs'] = []
                        airports[arpt_id]['pp'] = []
                        airports[arpt_id]['msas'] = []
                    elif sub_code == 'C':
                        airports[arpt_id]['wpts'][rec['wpt_ident']] = rec
                        waypoints[rec['wpt_ident']] = rec
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