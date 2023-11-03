set terminal pdfcairo enhanced color dashed font "Alegreya, 14" \
rounded size 16 cm, 9.6 cm

# Default encoding, line styles, pallette, border and grid are set in
# /gnuplotrc

set title "Decoding time comparison"
set logscale x 10
set xlabel "Iterations"
set xrange [100:500]
set ylabel "Time (s)"
set grid
set key right bottom
set key samplen 2 spacing 1 font "0,9"
set output "dec.pdf"
plot "dec/data_aes-128-cbc.dat" with line ls 1 title "AES-128-cbc", \
     "dec/data_aes-128-ofb.dat" with line ls 2 title "AES-128-ofb", \
     "dec/data_camellia-128-cbc.dat" with line ls 3 title "Camellia-128-cbc", \
     "dec/data_camellia-128-ofb.dat" with line ls 4 title "Camellia-128-ofb", \
     "dec/data_aria-128-cbc.dat" with line ls 5 title "Aria-128-cbc", \
     "dec/data_aria-128-ofb.dat" with line ls 7 title "Aria-128-ofb", \
     "dec/data_seed-cbc.dat" with line ls 6 title "Seed-cbc", \
     "dec/data_seed-ofb.dat" with line ls 8 title "Seed-ofb"
