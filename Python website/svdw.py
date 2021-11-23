import csv
from datetime import datetime
namen = {"Anton Vanhauwere": 0, "Dries Hofman": 0, "Dries Uytterhaegen": 0, "Emiel van Wetter": 0, "Gilles Speltincx": 0, "Isaak Noerens": 0, "Jari Verhecken": 0, "Jens De Temmerman": 0, "Jens Lateur": 0, "Jona Vangansbeke": 0, "Lucas Ardyns": 0, "Maarten Van Snick": 0, "Marcel Machiels": 0,
         "Mathias Schepers": 0, "Matthias Callebaut": 0, "Matthieu De Pauw": 0, "Mauritz Carlier": 0, "Michiel Degroote": 0, "Miel Herreman": 0, "Nisse Verstuyft": 0, "Reggie Demoor": 0, "Sem Backaert": 0, "Thomas Schepers": 0, "Tim Notebaert": 0, "Wout Van der Meulen": 0}
lineCount = 0
with open('Speler Van De Week.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    with open('SVDW.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        for row in reader:
            if lineCount == 0:
                writer.writerow(
                    [('Date this file was created: %s' % datetime.now().strftime('%x'))])
                writer.writerow(['Naam schrijver formulier',
                                'Nummer 1', 'Nummer 2', 'Nummer 3', 'Datum ingediend', 'Opmerkingen'])
                lineCount += 1
            data = []
            data += [row['voornaam'] + ' ' + row['naam']]
            data += [row['nr1']] + [row['nr2']] + [row['nr3']]
            datum = datetime.strptime(row['created_at'][:10], '%Y-%m-%d')
            data += [' ' + datum.strftime('%d') + ' ' +
                     datum.strftime('%B') + ' ' + datum.strftime('%Y')]
            data += [row['opmerking']]
            writer.writerow(data)
            namen[row['nr1']] += 3
            namen[row['nr2']] += 2
            namen[row['nr3']] += 1
            lineCount += 1
        writer.writerow('')
        namen = dict(sorted(namen.items(), key=lambda item: item[1]))
        for k, v in namen.items():
            writer.writerow([k, v])
        writer.writerow('')
        lineCount -= 1
        writer.writerow(['Aantal Personen die stemden', lineCount])
