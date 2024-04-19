#!/bin/bash

socat -dd TCP-LISTEN:1737,fork EXEC:/app/main