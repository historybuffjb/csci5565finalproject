
#version 3.5

global_settings {
    assumed_gamma 1
}
        
light_source {
    <200, 200, 200>*10000
    rgb 1.3
}
        
camera {
  location    <400, 400, 800>
  direction   y
  sky         z
  up          z
  right       (4/3)*x
  look_at     <0.0, 0, 1.2>
  angle       20
}
        
background {
    color rgb <0.60, 0.70, 0.95>
}
        
plane {
  z, -10

  texture {
    pigment {
      bozo
      color_map {
        [ 0.0 color rgb<0.356, 0.321, 0.274> ]
        [ 0.1 color rgb<0.611, 0.500, 0.500> ]
        [ 0.4 color rgb<0.745, 0.623, 0.623> ]
        [ 1.0 color rgb<0.837, 0.782, 0.745> ]
      }
      warp { turbulence 0.6 }
    }
    finish {
      diffuse 0.6
      ambient 0.1
      specular 0.2
      reflection {
        0.2, 0.6
        fresnel on
      }
      conserve_energy
    }
  }
}
        
#declare Mesh_Texture=
  texture{
    pigment{
      uv_mapping
      spiral2 8
      color_map {
        [0.5 color rgb 1 ]
        [0.5 color rgb <0,0,0.2> ]
      }
      scale 0.8
    }
    finish {
      specular 0.3
      roughness 0.01
    }
}
        
#declare Mesh=
mesh2 {
    vertex_vectors {
        152,
        <-36.067100524902344, -14.798500061035156, -4.116000175476074>, <-18.497299194335938, -14.798500061035156, 2.031899929046631>, <-18.497299194335938, 14.798500061035156, 2.031899929046631>,
		<-36.067100524902344, 14.798500061035156, -4.116000175476074>, <9.999999747378752e-05, -14.798500061035156, 4.116099834442139>, <9.999999747378752e-05, 14.798500061035156, 4.116099834442139>,
		<18.497400283813477, -14.798500061035156, 2.031899929046631>, <18.497400283813477, 14.798500061035156, 2.031899929046631>, <36.067298889160156, -14.798500061035156, -4.116099834442139>,
		<36.067298889160156, 14.798500061035156, -4.116099834442139>, <-17.757400512695312, -13.756099700927734, -0.06520000100135803>, <-34.6244010925293, -13.756099700927734, -5.967199802398682>,
		<-17.757400512695312, 13.755999565124512, -0.06520000100135803>, <-34.6244010925293, 13.755999565124512, -5.967199802398682>, <9.999999747378752e-05, -13.756099700927734, 1.9356000423431396>,
		<9.999999747378752e-05, 13.755999565124512, 1.9356000423431396>, <17.75749969482422, -13.756099700927734, -0.06520000100135803>, <17.75749969482422, 13.755999565124512, -0.06520000100135803>,
		<34.62459945678711, -13.756099700927734, -5.967199802398682>, <34.62459945678711, 13.755999565124512, -5.967199802398682>, <-36.067100524902344, -14.798500061035156, -4.392300128936768>,
		<-18.497299194335938, -14.798500061035156, 1.7555999755859375>, <-18.497299194335938, 14.798500061035156, 1.7555999755859375>, <-36.067100524902344, 14.798500061035156, -4.392300128936768>,
		<9.999999747378752e-05, -14.798500061035156, 3.8396999835968018>, <9.999999747378752e-05, 14.798500061035156, 3.8396999835968018>, <18.497400283813477, -14.798500061035156, 1.7555999755859375>,
		<18.497400283813477, 14.798500061035156, 1.7555999755859375>, <36.067298889160156, -14.798500061035156, -4.392399787902832>, <36.067298889160156, 14.798500061035156, -4.392399787902832>,
		<-34.6244010925293, -13.756099700927734, -4.187099933624268>, <-17.757400512695312, -13.756099700927734, 1.715000033378601>, <-17.757400512695312, 13.755999565124512, 1.715000033378601>,
		<-34.6244010925293, 13.755999565124512, -4.187099933624268>, <9.999999747378752e-05, -13.756099700927734, 3.7156999111175537>, <9.999999747378752e-05, 13.755999565124512, 3.7156999111175537>,
		<17.75749969482422, -13.756099700927734, 1.714900016784668>, <17.75749969482422, 13.755999565124512, 1.714900016784668>, <34.62459945678711, -13.756099700927734, -4.187099933624268>,
		<34.62459945678711, 13.755999565124512, -4.187099933624268>, <18.9596004486084, -6.979100227355957, -10.73799991607666>, <19.149799346923828, -6.979100227355957, -11.14579963684082>,
		<18.9596004486084, -7.428999900817871, -10.73799991607666>, <18.769500732421875, -6.979100227355957, -10.3302001953125>, <18.9596004486084, -6.529099941253662, -10.73799991607666>,
		<19.149799346923828, -6.979100227355957, -11.14579963684082>, <31.73270034790039, -6.979100227355957, -4.935200214385986>, <31.542600631713867, -7.428999900817871, -4.527400016784668>,
		<31.352399826049805, -6.979100227355957, -4.11959981918335>, <31.542600631713867, -6.529099941253662, -4.527400016784668>, <31.73270034790039, -6.979100227355957, -4.935200214385986>,
		<31.542600631713867, -6.979100227355957, -4.527400016784668>, <18.9596004486084, 6.828100204467773, -10.73799991607666>, <19.149799346923828, 6.828100204467773, -11.14579963684082>,
		<18.9596004486084, 6.3780999183654785, -10.73799991607666>, <18.769500732421875, 6.828100204467773, -10.3302001953125>, <18.9596004486084, 7.27810001373291, -10.73799991607666>,
		<19.149799346923828, 6.828100204467773, -11.14579963684082>, <31.73270034790039, 6.828100204467773, -4.935200214385986>, <31.542600631713867, 6.3780999183654785, -4.527400016784668>,
		<31.352399826049805, 6.828100204467773, -4.11959981918335>, <31.542600631713867, 7.27810001373291, -4.527400016784668>, <31.73270034790039, 6.828100204467773, -4.935200214385986>,
		<31.542600631713867, 6.828100204467773, -4.527400016784668>, <25.38479995727539, -6.35830020904541, -23.47439956665039>, <25.38479995727539, 5.739999771118164, -23.47439956665039>,
		<25.38479995727539, 5.739999771118164, -12.119000434875488>, <25.38479995727539, -6.35830020904541, -12.119000434875488>, <19.866300582885742, -6.35830020904541, -23.47439956665039>,
		<19.866300582885742, -6.35830020904541, -12.119000434875488>, <19.866300582885742, 5.739999771118164, -12.119000434875488>, <19.866300582885742, 5.739999771118164, -23.47439956665039>,
		<25.38479995727539, -6.35830020904541, -23.47439956665039>, <25.38479995727539, -6.35830020904541, -12.119000434875488>, <19.866300582885742, -6.35830020904541, -12.119000434875488>,
		<19.866300582885742, -6.35830020904541, -23.47439956665039>, <25.38479995727539, 5.739999771118164, -12.119000434875488>, <19.866300582885742, -6.35830020904541, -12.119000434875488>,
		<25.38479995727539, 5.739999771118164, -12.119000434875488>, <25.38479995727539, 5.739999771118164, -23.47439956665039>, <19.866300582885742, 5.739999771118164, -23.47439956665039>,
		<19.866300582885742, 5.739999771118164, -12.119000434875488>, <25.38479995727539, 5.739999771118164, -23.47439956665039>, <19.866300582885742, -6.35830020904541, -23.47439956665039>,
		<-19.58060073852539, -6.35830020904541, -23.47439956665039>, <-19.58060073852539, 5.739999771118164, -23.47439956665039>, <-19.58060073852539, 5.739999771118164, -12.119000434875488>,
		<-19.58060073852539, -6.35830020904541, -12.119000434875488>, <-25.099199295043945, -6.35830020904541, -23.47439956665039>, <-25.099199295043945, -6.35830020904541, -12.119000434875488>,
		<-25.099199295043945, 5.739999771118164, -12.119000434875488>, <-25.099199295043945, 5.739999771118164, -23.47439956665039>, <-19.58060073852539, -6.35830020904541, -23.47439956665039>,
		<-19.58060073852539, -6.35830020904541, -12.119000434875488>, <-25.099199295043945, -6.35830020904541, -12.119000434875488>, <-25.099199295043945, -6.35830020904541, -23.47439956665039>,
		<-19.58060073852539, 5.739999771118164, -12.119000434875488>, <-25.099199295043945, -6.35830020904541, -12.119000434875488>, <-19.58060073852539, 5.739999771118164, -12.119000434875488>,
		<-19.58060073852539, 5.739999771118164, -23.47439956665039>, <-25.099199295043945, 5.739999771118164, -23.47439956665039>, <-25.099199295043945, 5.739999771118164, -12.119000434875488>,
		<-19.58060073852539, 5.739999771118164, -23.47439956665039>, <-25.099199295043945, -6.35830020904541, -23.47439956665039>, <5.342899799346924, 7.836900234222412, -59.977500915527344>,
		<5.342899799346924, 7.836900234222412, -66.41690063476562>, <-5.431700229644775, 7.836900234222412, -66.41690063476562>, <-5.431700229644775, 7.836900234222412, -59.977500915527344>,
		<13.456999778747559, 7.836900234222412, -52.01499938964844>, <-19.263999938964844, 7.836900234222412, -32.9739990234375>, <19.29640007019043, 7.836900234222412, -39.80590057373047>,
		<-19.263999938964844, 7.836900234222412, -10.812999725341797>, <-29.36549949645996, 7.836900234222412, -3.578200101852417>, <-17.777700424194336, 7.836900234222412, 0.3824000060558319>,
		<0.016200000420212746, 7.836900234222412, 2.4010000228881836>, <19.29640007019043, 7.836900234222412, -0.24250000715255737>, <-5.431700229644775, 7.31689977645874, -66.93689727783203>,
		<-5.951700210571289, 7.31689977645874, -66.41690063476562>, <-5.951700210571289, 7.31689977645874, -60.39469909667969>, <-19.784000396728516, 7.31689977645874, -33.35770034790039>,
		<-19.784000396728516, 7.31689977645874, -11.009499549865723>, <19.8164005279541, 7.31689977645874, -40.06990051269531>, <19.8164005279541, 7.31689977645874, -0.24250000715255737>,
		<13.97700023651123, 7.31689977645874, -52.423500061035156>, <5.8628997802734375, 7.31689977645874, -60.39469909667969>, <5.8628997802734375, 7.31689977645874, -66.41690063476562>,
		<5.342899799346924, 7.31689977645874, -66.93689727783203>, <-5.951700210571289, -7.302000045776367, -66.41690063476562>, <-5.431700229644775, -7.302000045776367, -66.93689727783203>,
		<-5.951700210571289, -7.302000045776367, -60.39469909667969>, <-19.784000396728516, -7.302000045776367, -33.35770034790039>, <-19.784000396728516, -7.302000045776367, -11.009599685668945>,
		<19.8164005279541, -7.302000045776367, -40.06990051269531>, <19.8164005279541, -7.302000045776367, -0.24250000715255737>, <13.97700023651123, -7.302000045776367, -52.423500061035156>,
		<5.8628997802734375, -7.302000045776367, -60.39469909667969>, <5.8628997802734375, -7.302000045776367, -66.41690063476562>, <5.342899799346924, -7.302000045776367, -66.93689727783203>,
		<-5.431700229644775, -7.822000026702881, -66.41690063476562>, <-5.431700229644775, -7.822000026702881, -59.977500915527344>, <-19.263999938964844, -7.822000026702881, -32.9739990234375>,
		<-19.263999938964844, -7.822000026702881, -10.812999725341797>, <19.29640007019043, -7.822000026702881, -39.80590057373047>, <19.29640007019043, -7.822000026702881, -0.24250000715255737>,
		<13.456999778747559, -7.822000026702881, -52.01499938964844>, <5.342899799346924, -7.822000026702881, -59.977500915527344>, <5.342899799346924, -7.822000026702881, -66.41690063476562>,
		<0.016200000420212746, -7.822000026702881, 2.4010000228881836>, <-17.777700424194336, -7.822000026702881, 0.3824000060558319>, <-29.36549949645996, -7.822000026702881, -3.578200101852417>,
		<-29.885499954223633, 7.31689977645874, -3.9400999546051025>, <-29.885499954223633, -7.302000045776367, -3.9400999546051025>, 
    }
    face_indices {
        224,
        <0, 1, 2>, <2, 3, 0>,
		<1, 4, 5>, <5, 2, 1>,
		<4, 6, 7>, <7, 5, 4>,
		<6, 8, 9>, <9, 7, 6>,
		<10, 11, 12>, <13, 12, 11>,
		<14, 10, 15>, <12, 15, 10>,
		<16, 14, 17>, <15, 17, 14>,
		<18, 16, 19>, <17, 19, 16>,
		<1, 0, 20>, <20, 21, 1>,
		<3, 2, 22>, <22, 23, 3>,
		<0, 3, 23>, <23, 20, 0>,
		<4, 1, 21>, <21, 24, 4>,
		<2, 5, 25>, <25, 22, 2>,
		<6, 4, 24>, <24, 26, 6>,
		<5, 7, 27>, <27, 25, 5>,
		<8, 6, 26>, <26, 28, 8>,
		<9, 8, 28>, <28, 29, 9>,
		<7, 9, 29>, <29, 27, 7>,
		<21, 20, 30>, <30, 31, 21>,
		<23, 22, 32>, <32, 33, 23>,
		<20, 23, 33>, <33, 30, 20>,
		<24, 21, 31>, <31, 34, 24>,
		<22, 25, 35>, <35, 32, 22>,
		<26, 24, 34>, <34, 36, 26>,
		<25, 27, 37>, <37, 35, 25>,
		<28, 26, 36>, <36, 38, 28>,
		<29, 28, 38>, <38, 39, 29>,
		<27, 29, 39>, <39, 37, 27>,
		<31, 30, 11>, <11, 10, 31>,
		<33, 32, 12>, <12, 13, 33>,
		<30, 33, 13>, <13, 11, 30>,
		<34, 31, 10>, <10, 14, 34>,
		<32, 35, 15>, <15, 12, 32>,
		<36, 34, 14>, <14, 16, 36>,
		<35, 37, 17>, <17, 15, 35>,
		<38, 36, 16>, <16, 18, 38>,
		<39, 38, 18>, <18, 19, 39>,
		<37, 39, 19>, <19, 17, 37>,
		<40, 41, 42>, <40, 42, 43>,
		<40, 43, 44>, <40, 44, 45>,
		<41, 46, 47>, <41, 47, 42>,
		<42, 47, 48>, <42, 48, 43>,
		<43, 48, 49>, <43, 49, 44>,
		<44, 49, 50>, <44, 50, 45>,
		<51, 47, 46>, <51, 48, 47>,
		<51, 49, 48>, <51, 50, 49>,
		<52, 53, 54>, <52, 54, 55>,
		<52, 55, 56>, <52, 56, 57>,
		<53, 58, 59>, <53, 59, 54>,
		<54, 59, 60>, <54, 60, 55>,
		<55, 60, 61>, <55, 61, 56>,
		<56, 61, 62>, <56, 62, 57>,
		<63, 59, 58>, <63, 60, 59>,
		<63, 61, 60>, <63, 62, 61>,
		<64, 65, 66>, <66, 67, 64>,
		<68, 69, 70>, <70, 71, 68>,
		<72, 73, 74>, <74, 75, 72>,
		<67, 76, 70>, <70, 77, 67>,
		<78, 79, 80>, <80, 81, 78>,
		<82, 64, 83>, <83, 71, 82>,
		<84, 85, 86>, <86, 87, 84>,
		<88, 89, 90>, <90, 91, 88>,
		<92, 93, 94>, <94, 95, 92>,
		<87, 96, 90>, <90, 97, 87>,
		<98, 99, 100>, <100, 101, 98>,
		<102, 84, 103>, <103, 91, 102>,
		<104, 105, 106>, <106, 107, 104>,
		<108, 104, 107>, <107, 109, 108>,
		<109, 110, 108>, <111, 112, 113>,
		<111, 113, 114>, <109, 111, 114>,
		<109, 114, 115>, <109, 115, 110>,
		<106, 116, 117>, <118, 107, 106>,
		<106, 117, 118>, <119, 109, 107>,
		<107, 118, 119>, <109, 119, 120>,
		<120, 111, 109>, <121, 110, 115>,
		<115, 122, 121>, <123, 108, 110>,
		<110, 121, 123>, <124, 104, 108>,
		<108, 123, 124>, <125, 105, 104>,
		<104, 124, 125>, <105, 125, 126>,
		<116, 106, 105>, <105, 126, 116>,
		<127, 117, 116>, <116, 128, 127>,
		<129, 118, 117>, <117, 127, 129>,
		<130, 119, 118>, <118, 129, 130>,
		<130, 131, 120>, <120, 119, 130>,
		<132, 121, 122>, <122, 133, 132>,
		<134, 123, 121>, <121, 132, 134>,
		<135, 124, 123>, <123, 134, 135>,
		<136, 125, 124>, <124, 135, 136>,
		<137, 126, 125>, <125, 136, 137>,
		<128, 116, 126>, <126, 137, 128>,
		<128, 138, 127>, <139, 129, 127>,
		<127, 138, 139>, <140, 130, 129>,
		<129, 139, 140>, <140, 141, 131>,
		<131, 130, 140>, <142, 132, 133>,
		<133, 143, 142>, <144, 134, 132>,
		<132, 142, 144>, <145, 135, 134>,
		<134, 144, 145>, <146, 136, 135>,
		<135, 145, 146>, <136, 146, 137>,
		<138, 128, 137>, <137, 146, 138>,
		<142, 143, 147>, <148, 149, 141>,
		<147, 148, 141>, <142, 147, 141>,
		<142, 141, 140>, <144, 142, 140>,
		<140, 139, 145>, <145, 144, 140>,
		<139, 138, 146>, <146, 145, 139>,
		<150, 151, 149>, <149, 148, 113>,
		<150, 149, 113>, <112, 150, 113>,
		<143, 133, 122>, <143, 122, 115>,
		<143, 115, 114>, <147, 143, 114>,
		<150, 112, 111>, <111, 120, 150>,
		<151, 150, 120>, <120, 131, 151>,
		<149, 151, 131>, <131, 141, 149>,
		<147, 114, 113>, <113, 148, 147>,

    }
}
        
object {
  Mesh
  texture { Mesh_Texture }
  rotate 180*z
  rotate 90*x
  translate < -2, 2, 1.5>
}
        