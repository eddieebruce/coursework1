from flask import Flask, render_template, url_for, abort
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('base.html'), 200

@app.route('/Playstation4/')
def root_Playstation4():
  return render_template('Playstation4.html'), 200

@app.route('/XboxOne/')
def root_XboxOne():
  return render_template('Xboxone.html'), 200

@app.route('/WiiU/')
def root_WiiU():
  return render_template('Wiiu.html'), 200

@app.route('/uncharted4/')
def root_uncharted4():
  return render_template('uncharted4.html'), 200

@app.route('/halo5/')
def root_halo5():
  return render_template('halo5.html'), 200

@app.route('/smashbrosu/')
def root_smashbrosu():
  return render_template('smashbrosu.html'), 200

@app.route('/thelastofus/')
def root_thelastofus():
  return render_template('thelastofus.html'), 200

@app.route('/rarereplay/')
def root_rarereplay():
  return render_template('rarereplay.html'), 200

@app.route('/mariokart8/')
def root_mariokart8():
  return render_template('mariokart8.html'), 200

@app.route('/infamous/')
def root_infamous():
  return render_template('infamous.html'), 200

@app.route('/deadrising3/')
def root_deadrising3():
  return render_template('deadrising3.html'), 200

@app.route('/supermariomaker/')
def root_supermariomaker():
  return render_template('supermariomaker.html'), 200

@app.route('/bioshock/')
def root_bioshock():
  return render_template('bioshock.html'), 200

@app.route('/tombraider/')
def root_tombraider():
  return render_template('tombraider.html'), 200

@app.route('/supermario3dworld/')
def root_supermario3dworld():
  return render_template('supermario3dworld.html'), 200

@app.route('/raymanlegends/')
def root_raymanlegends():
  return render_template('raymanlegends.html'), 200

@app.route('/dyinglight/')
def root_dyinglight():
  return render_template('dyinglight.html'), 200

@app.route('/windwaker/')
def root_windwaker():
  return render_template('windwaker.html'), 200

@app.route('/batman/')
def root_batman():
  return render_template('batman.html'), 200

@app.route('/starfoxzero/')
def starfoxzero():
  return render_template('starfoxzero.html'), 200

@app.route('/metalgearsolidv/')
def root_metalgearsolidv():
  return render_template('metalgearsolidv.html'), 200

@app.route('/twilightprincesshd/')
def root_twilightprincess():
  return render_template('twilightprincesshd.html'), 200

@app.route('/fallout4/')
def root_fallout4():
  return render_template('fallout4.html'), 200

@app.route('/pikmin3/')
def root_pikmin3():
  return render_template('pikmin3.html'), 200

@app.route('/bloodborne/')
def root_bloodborne():
  return render_template('bloodborne.html'), 200

@app.route('/killerinstinct/')
def root_killerinstinct():
  return render_template('killerinstinct.html'), 200

@app.route('/splatoon/')
def root_splatoon():
  return render_template('splatoon.html'), 200

@app.route('/codghosts/')
def root_codghosts():
  return render_template('codghosts.html'), 200

@app.route('/untildawn/')
def root_untildawn():
  return render_template('untildawn.html'), 200

@app.route('/godofwar3/')
def root_godofwar3():
  return render_template('godofwar3.html'), 200

@app.route('/unchartedtndc/')
def root_unchartedtndc():
  return render_template('unchartedtndc.html'), 200

@app.route('/ratchetandclank/')
def root_ratchetandclank():
  return render_template('ratchetandclank.html'), 200

@app.route('/driveclub/')
def root_driveclub():
  return render_template('driveclub.html'), 200

@app.route('/nomanssky/')
def root_nomanssky():
  return render_template('nomanssky.html'), 200

@app.route('/gtav/')
def root_gtav():
  return render_template('gtav.html'), 200

@app.route('/destiny/')
def root_destiny():
  return render_template('destiny.html'), 200

@app.route('/guitarherolive/')
def root_guitarherolive():
  return render_template('guitarherolive.html'), 200

@app.route('/codblackops2/')
def root_codblackops2():
  return render_template('codblackops2.html'), 200

@app.route('/nba2k16/')
def root_nba2k16():
  return render_template('nba2k16.html'), 200

@app.route('/darksouls3/')
def root_darksouls3():
  return render_template('darksouls3.html'), 200

@app.route('/thewitcher/')
def root_thewitcher():
  return render_template('thewitcher.html'), 200

@app.route('/quantumbreak/')
def root_quantumbreak():
  return render_template('quantumbreak.html'), 200

@app.route('/forza5/')
def root_forza5():
  return render_template('forza5.html'), 200

@app.route('/sunsetoverdrive/')
def root_sunsetoverdrive():
  return render_template('sunsetoverdrive.html'), 200

@app.route('/gearsofwar4/')
def root_gearsofwar4():
  return render_template('gearsofwar4.html'), 200

@app.route('/halotmcc/')
def root_halotmcc():
  return render_template('halotmcc.html'), 200

@app.route('/titanfall/')
def root_titanfall():
  return render_template('titanfall.html'), 200

@app.route('/hyrulewarriors/')
def root_hyrulewarriors():
  return render_template('hyrulewarriors.html'), 200

@app.route('/bayonetta/')
def root_bayonetta():
  return render_template('bayonetta.html'), 200

@app.route('/donkeykongcountry/')
def root_donkeykongcountry():
  return render_template('donkeykongcountry.html'), 200

@app.route('/newsupermariobrosu/')
def root_newsupermariobrosu():
  return render_template('newsupermariobrosu.html'), 200

@app.route('/nintendoland/')
def root_nintendoland():
  return render_template('nintendoland.html'), 200

@app.route('/yoshiswoollyworld/')
def root_yoshiswoollyworld():
  return render_template('yoshiswoollyworld.html'), 200

@app.route('/pokkentournament/')
def root_pokkentournament():
  return render_template('pokkentournament.html'), 200

@app.route('/xenobladechroniclesx/')
def root_xenobladechroniclesx():
  return render_template('xenobladechroniclesx.html'), 200

@app.route('/thewonderful101/')
def root_thewonderful101():
  return render_template('thewonderful101.html'), 200

@app.route('/marioandsonic/')
def root_marioandsonic():
  return render_template('marioandsonic.html'), 200

@app.route('/captaintoad/')
def root_captaintoad():
  return render_template('captaintoad.html'), 200

@app.route('/gameandwario/')
def root_gameandwario():
  return render_template('gameandwario.html'), 200

@app.route('/soniclostworld/')
def root_soniclostworld():
  return render_template('soniclostworld.html'), 200



if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

