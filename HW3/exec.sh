#!/bin/bash

#$1=mode
#$2=priv or pub(RSA or DSA)
#$3 and $4=output sign or signature input

time openssl dgst -sha256 -$1 $2 -$3 $4 image.jpg 2> >(grep "real" | awk '{print $2}' >&2) 1>/dev/null

  
