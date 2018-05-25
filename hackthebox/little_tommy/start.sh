#!/bin/bash
socat TCP-LISTEN:8887,reuseaddr,fork EXEC:"./little_tommy",pty
