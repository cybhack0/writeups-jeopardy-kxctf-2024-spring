#!/usr/bin/env bash
set -e
exec socat -dd tcp-listen:11337,fork exec:./not_my_format
