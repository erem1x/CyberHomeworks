set terminal pdfcairo enhanced color dashed font "Alegreya, 14" \
rounded size 16 cm, 9.6 cm

# Default encoding, line styles, pallette, border and grid are set in
# /gnuplotrc

set title "Cipher comparison"
#set logscale x 10
set xlabel "Iterations"
#set xrange [100:500]
set ylabel "Time (s)"
set grid
set key left top
set key samplen 2 spacing 1 font "0,9"
set output "comparison.pdf"
plot "data/data_aes-128-cbc.dat" with line ls 1 title "AES-128-cbc", \
     "data/data_aes-128-ofb.dat" with line ls 2 title "AES-128-ofb", \
     "data/data_aes-256-cbc.dat" with line ls 3 title "AES-256-cbc", \
     "data/data_aes-256-ofb.dat" with line ls 4 title "AES-256-ofb", \
     "data/data_camellia-128-cbc.dat" with line ls 5 title "Camellia-128-cbc", \
     "data/data_camellia-128-ofb.dat" with line ls 6 title "Camellia-128-ofb", \
     "data/data_aria-128-cbc.dat" with line ls 7 title "Aria-128-cbc", \
     "data/data_aria-128-ofb.dat" with line ls 8 title "Aria-128-ofb", \

