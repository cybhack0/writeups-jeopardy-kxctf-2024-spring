#!/usr/bin/env bash
set -e
exec socat -dd tcp-listen:13337,fork exec:./zeros_or_nulls
