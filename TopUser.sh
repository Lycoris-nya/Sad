#!/bin/bash
 cat $1 | cut -f 4 -d ' ' | sort | uniq -c | sort | tail -n 10