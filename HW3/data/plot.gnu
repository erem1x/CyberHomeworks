set terminal pdfcairo enhanced color dashed font "Alegreya, 14" \
rounded size 16 cm, 9.6 cm

set title "RSA vs DSA"
set ylabel "Time (s)"
set yrange [65:85]
set grid
set output "comparison.pdf"
set xtics ("Signature" 0.25, "Verification" 1.75)


set boxwidth 0.5
set style fill solid

plot 'data.dat' every 2  using 1:2 with boxes ls 1 title "RSA", \
     'data.dat' every 2::1 using 1:2 with boxes ls 2 title "DSA"
