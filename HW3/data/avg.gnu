set terminal pdfcairo enhanced color dashed font "Alegreya, 14" \
rounded size 16 cm, 9.6 cm

set title "Average time"
set ylabel "Time (s)"
set yrange [0:]
set grid
set output "average.pdf"
set xtics ("Signature" 0.25, "Verification" 1.75)


set boxwidth 0.5
set style fill solid

plot 'avg_data.dat' every 2    using 1:2 with boxes ls 1 title "RSA", \
     'avg_data.dat' every 2::1 using 1:2 with boxes ls 2 title "DSA"
