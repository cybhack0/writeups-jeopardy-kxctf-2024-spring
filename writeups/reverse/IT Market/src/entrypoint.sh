#!/bin/bash

socat -dd TCP-LISTEN:1228,fork EXEC:/app/main