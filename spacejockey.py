from flask import Flask
from flask import render_template
import json
import ephem

app = Flask(__name__)

lines_iss =[]
lines_iss.append('1 25544U 98067A   17118.86658832 +.00003789 +00000-0 +64904-4 0  9998')
lines_iss.append('2 25544 051.6427 284.1335 0005712 103.4876 046.8313 15.53931139054089')

tle_iss = ephem.readtle("ISS", lines_iss[0], lines_iss[1])

lines_aqua = []
lines_aqua.append('1 27424U 02022A   17118.92920056 +.00000140 +00000-0 +41123-4 0  9996')
lines_aqua.append('2 27424 098.2013 060.9656 0000079 026.8795 023.5764 14.57120412797051')

tle_aqua = ephem.readtle('EOS Aqua', lines_aqua[0], lines_aqua[1])

lines_terra = []
lines_terra.append('1 25994U 99068A   17118.76280116 +.00000128 +00000-0 +38489-4 0  9997')
lines_terra.append('2 25994 098.2110 194.5047 0000813 099.8748 260.2521 14.57108495923476')

tle_terra = ephem.readtle('EOS Aqua', lines_terra[0], lines_terra[1])


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/sat_locs")
def satellites_location():
	tle_iss.compute()
	tle_terra.compute()
	tle_aqua.compute()
	json2 =json.dumps({"iss": (str(tle_iss.sublat), str(tle_iss.sublong)),
		"terra": (str(tle_terra.sublat), str(tle_terra.sublong)),
		"aqua": (str(tle_aqua.sublat), str(tle_aqua.sublong))})
	return json2

if __name__ == "__main__":
    app.run()