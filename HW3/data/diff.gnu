set terminal pdfcairo enhanced color dashed font "Alegreya, 14" \
rounded size 16 cm, 9.6 cm

set title "Net difference"
#set yrange [0.5:0.5]
set ylabel "Time (s)"
set grid
set key left top
set key samplen 2 spacing 1 font "0,9"
set output "diff.pdf"
plot "diff.dat" using 1:2 with line ls 1 title "Signature", \
  "" using 1:3 with line ls 2 title "Verification"
