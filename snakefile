rule count:
    input:
        'coursesTaken-B.csv'
    output:
        'coursesTaken-B.txt'
    shell:
        'python3 count.py {input} {output}'