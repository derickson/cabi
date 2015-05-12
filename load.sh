#!/bin/sh

cat "CapitalbikeshareData/Source CapitalBikeshare Data/2010-Q4-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2011-Q1-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2011-Q2-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2011-Q3-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2011-Q4-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2012-Q1-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2012-Q2-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2012-Q3-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2012-Q4-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2013-Q1-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2013-Q2-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2013-Q3-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat1.conf

cat "CapitalbikeshareData/Source CapitalBikeshare Data/2013-Q4-Trips-History-Data2.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat2.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2014-Q1-Trips-History-Data2.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat2.conf
cat "CapitalbikeshareData/Source CapitalBikeshare Data/2014-Q2-Trips-History-Data2.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat2.conf


cat "CapitalbikeshareData/Source CapitalBikeshare Data/2014-Q3-Trips-History-Data3.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat3.conf

cat "CapitalbikeshareData/Source CapitalBikeshare Data/2014-Q4-Trips-History-Data.csv" | sed -e "1d" | /Users/dave/dev/logstash/logstash-1.4.2/bin/logstash --pluginpath . -f bikeshareFormat4.conf