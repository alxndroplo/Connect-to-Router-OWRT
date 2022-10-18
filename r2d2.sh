#!/bin/bash
set -xv
DebugF=debug_115.txt
PassF=pass115.txt
DebugF116=debug_116.txt
PassF116=pass116.txt
DebugF117=debug_117.txt
PassF117=pass117.txt

while read line
do
  echo "$line"
echo "---------------------------------------------------------------" >>$DebugF
echo `date` $line >>$DebugF
RESULT=`./r2d2.py $line >>$DebugF`
echo "---------------------------------------------------------------" >>$DebugF
done <$PassF

while read line
do
  echo "$line"
echo "---------------------------------------------------------------" >>$DebugF116
echo `date` $line >>$DebugF116
RESULT=`./r2d2.py $line >>$DebugF116`
echo "---------------------------------------------------------------" >>$DebugF116
done <$PassF116

while read line
do
  echo "$line"
echo "---------------------------------------------------------------" >>$DebugF117
echo `date` $line >>$DebugF117
RESULT=`./r2d2.py $line >>$DebugF117`
echo "---------------------------------------------------------------" >>$DebugF117
done <$PassF117

