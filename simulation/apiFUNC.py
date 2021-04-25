import asyncio
import json
import sys
import re 
from pprint import pprint
import spacetrack.operators as op
from spacetrack.aio import AsyncSpaceTrackClient

def apiCALL(SatID):
    async def download_latest_tles():
        st = AsyncSpaceTrackClient(identity='jts0079@auburn.edu',
                                password='VMCAApassword21')

        async with st:
            data = await st.tle_latest(
                iter_lines=True, 
                ordinal=1, 
                epoch='>now-60',
                norad_cat_id = (SatID),
                orderby=['norad_cat_id'],
                format='tle')

            with open('step1.txt', 'w') as outfile:
                async for line in data:
                    outfile.write(line + ' $ ' +'\n' )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_latest_tles())

    with open('step2.txt', 'w') as outfile, open('step1.txt', 'r') as infile:
        for line in infile:
            outfile.write(line.replace('   ',' ').strip())
    i = 0
    with open('step2.txt', 'r') as infile:
        for line in infile:
            i = i+1
            line = line.strip()
            ldata = line.split('$')

    with open('step3.txt', 'w') as outfile:
        j = 0
        for m in ldata: 
            if (j % 2 ) == 0:
                tle = ldata[j]
            elif (j % 2 ) > 0:
                tle = ldata[j]
            data = tle.replace('  ',' ')
            outfile.write(data + '\n')
            j = j+1

    with open('step3.txt', 'r') as inF:
        tlelist = []
        count = 1
        for line in inF:
            line = line.rstrip()

            if count % 2 == 0:
                tlelist.append(old_line + ' ' + line)
            else: 
                old_line = line
            count += 1

    with open('step4.txt', 'w') as outF:
        satnum = 0
        for line in tlelist: 
            data = tlelist[satnum]
            outF.write(data + ' \n')
            satnum = satnum + 1

    counter =0
    with open('step4.txt', 'r') as data:
        for line in data:
            counter = counter+1
            line = line.strip()
            ld = line.split(' ')

            SatNum = ld[10]
            eccen = ld[13]
            inc = ld[11]
            ArgPer = ld[14]
            MeanAnom = ld[15]
            RAAN = ld[12]
            MMotion = ld[16]

            if counter == count-1:
                break
    checker = 11
    return(checker,SatNum,eccen,inc,ArgPer,MeanAnom,RAAN,MMotion)
