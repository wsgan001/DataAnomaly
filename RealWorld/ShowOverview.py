import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statistics
import Divergence
import math


jsd = [0.008748994684134268, 0.015240537320908422, 0.0015240513988232995, 0.0031051148679070014, 0.0033735233256568784, 0.002421185881730095, 0.0036073414352532987, 0.003849237851658265, 0.010703146709061117, 0.001975003412196996, 0.0032388009910297787, 0.0033171020847916253, 0.0022375245606253186, 0.008835788288123213, 0.002251804174186225, 0.012975544998831311, 0.0029251502647842263, 0.003520611946407365, 0.0027328098662684546, 0.004669021702278735, 0.004389173710159215, 0.0052263420164222665, 0.00925964078586519, 0.0019185349128100077, 0.003406742393244508, 0.0026002231282451225, 0.003045507093689207, 0.0067725270507850675, 0.004615923237517347, 0.009494840581165086, 0.0046539826922372025, 0.0029901092897060464, 0.0015919472396219618, 0.002341132882329799, 0.008668640534694039, 0.002719877015996795, 0.005893563638018638, 0.0023407478450889006, 0.0010666309765906018, 0.003181317882297267, 0.0008688960500944033, 0.0018644504769192028, 0.002971659222288935, 0.007900296035128162, 0.000539324172271058, 0.002070575204687525, 0.002406317190937706, 0.0025697463695358285, 0.007139095707732642, 0.004222044168417817, 0.007282998170726579, 0.011216860395627186, 0.008315359831170488, 0.004959953982169934, 0.0076942042005910555, 0.002873583360384834, 0.01007298973427609, 0.18211119159482825, 0.0531437787736118, 0.020538666252942844, 0.008202611396243096, 0.013486987254674272, 0.007025516692222527, 0.007968103980006257, 0.00565440793585731, 0.007850874676782024, 0.006883947056933503, 0.004533591600688811, 0.0074019467571685696, 0.007666759799457192, 0.0020304089373184312, 0.008168592036003026, 0.006297009040415333, 0.006545417318380353, 0.004279373035834545, 0.005463314780357911, 0.009132897705699949, 0.0012589590299461146, 0.003077497457671197, 0.007169884482741821, 0.006497335566025242, 0.005035924853373506, 0.005213834137590346, 0.010163536422927676, 0.0034621070971155832, 0.004928462153098465, 0.003895404550470798, 0.0029072073566535858, 0.003232659843453966, 0.003840357774316221, 0.01275522124106924, 0.001988635570324742, 0.011946891346651492, 0.001629165340951174, 0.0022818483445895647, 0.003944023254344372, 0.0024269528836270747, 0.006704720069243376, 0.0017179430545035484, 0.0068923543406214085, 0.0024687533177489215, 0.0021391592684809183, 0.003337229812832167, 0.003418460009092912, 0.00963774241925934, 0.0019908227765451374, 0.0085369465407919, 0.0022313013645565757, 0.0026349226184029582, 0.001866284445646571, 0.00453337010184295, 0.007959710325099978, 0.004286140741141147, 0.006479426746063331, 0.0070482861398849465, 0.003513510351339872, 0.004011216177183012, 0.0022158782594764465, 0.008482467574922936, 0.0018005973868901156, 0.006927645000266355, 0.0031788619299485516, 0.002827146060151168, 0.0027326713259520825, 0.0023513370068489726, 0.0034413868280844797, 0.0029409963734202743, 0.007653961969824965, 0.002333952196163844, 0.0011181270942302469, 0.0029508407614112046, 0.0021271743015999767, 0.004425760886956154, 0.002168421836833714, 0.012305351340361502, 0.0026827322564296416, 0.0019098908469046747, 0.0013592964300862566, 0.002380318485733921, 0.008394673464354855, 0.004556734738429836, 0.004469325735883187, 0.01574408344673982, 0.0019610301160683423, 0.0023490759532661027, 0.0037439040817400598, 0.006537844089600558, 0.00502209584745454, 0.00865884774549225, 0.003428085636320212, 0.0037721336253018815, 0.0022381926818572967, 0.0024972709191267745, 0.003696137837246074, 0.001495232459583108, 0.02259290285903107, 0.004747108468096055, 0.002821409752301705, 0.0016619797877835908, 0.0018547106975043703, 0.0030819951024492207, 0.0026091704366595545, 0.010266012627590158, 0.0028516783112439176, 0.0021412014560428243, 0.0033114344234404396, 0.001540835573547622, 0.00421042657083937, 0.001609677677026934, 0.010826776678340588, 0.003281086486635346, 0.003104976013677881, 0.0007294907035820844, 0.0013730124485286691, 0.0029796799855134745, 0.0033320783291904826, 0.006138875297775175, 0.0025269100477785253, 0.0018474482619564604, 0.006550181258772119, 0.006058177303177359, 0.003684488058162373, 0.0060383056125407585, 0.001998049651805986, 0.002513968582648026, 0.0038666068174424218, 0.014656122879418133, 0.011672860109471581, 0.006142586502766021, 0.0012173613424367746, 0.008857786961960937, 0.00385930985089498, 0.0034151708501511517, 0.005681893168830065, 0.00295904086741758, 0.0030945633988773064, 0.0025890161030214746, 0.00931731631094925, 0.0037796954562716407, 0.0024056415775821766, 0.0030189537084744393, 0.0024941422590980594, 0.0011302871904916953, 0.010338659020832449, 0.006384228024171711, 0.003107964928195201, 0.0030667869682372345, 0.0018064458231381573, 0.0023188327254547135, 0.006614682180564619, 0.0018241886947836265, 0.006805696163668241, 0.002559666832954304, 0.0025331049125342855, 0.0013611815815298394, 0.0002709540976480625, 0.0037241045005423764, 0.002376689343175004, 0.005225119164560578, 0.0012506956192081915, 0.01716175878580618, 0.004205132960958305, 0.003507711986412852, 0.009337160353107955, 0.003040117972305669, 0.002585514316955118, 0.002260336278832566, 0.0032094571197341334, 0.001460078946165939, 0.002736534340808948, 0.004419932719028959, 0.002733579737080539, 0.003587940703536317, 0.0016956952378995283, 0.005479556283897656, 0.0049320044354873235, 0.0015502869119702334, 0.010463913315544278, 0.003112910633934105, 0.0033806295197996283, 0.0027050788380969656, 0.0006166887812586972, 0.004075737582778353, 0.004530107416332196, 0.011411086147895688, 0.0015218294398832875, 0.0014176485128186052, 0.010083405442320186, 0.02365760149932455, 0.007721393362194236, 0.004868469935865827, 0.001116444356297833, 0.0024494117120294695, 0.0035745596680197096, 0.0021758238903891924, 0.0008367696176108553, 0.004703960603485181, 0.00287994622794217, 0.005897651935413488, 0.0022638294050707983, 0.0022425480930810737, 0.002010716636285551, 0.005485271402202439, 0.003923292536136854, 0.006514403929646487, 0.008280239501136408, 0.005168807505326366, 0.0024593596638259247, 0.0022910004466175343, 0.006632987130707922, 0.004132152533710266, 0.003218792726717057, 0.0026595223518779596, 0.004934047877792711, 0.0024624531209616607, 0.0025901914492929908, 0.002044777073571057, 0.005291756204156415, 0.003121458484824457, 0.006711224585810493, 0.002433222565360869, 0.0036495174298812956, 0.0014424453300211587, 0.0007164052802857296, 0.0043769117936971825, 0.00879621822274281, 0.007835843150318841, 0.004673343037982561, 0.003995782704419247, 0.002761337379385999, 0.0042885507731858724, 0.005233338118323313, 0.0037584392854631424, 0.005524618964267186, 0.004899969155736111]
jsd_cen = [0.11750792902637591, 0.12571643712922537, 0.1327371844763033, 0.14605149344605936, 0.07064098788528099, 0.0753906808102719, 0.0585394723758131, 0.07632265453659695, 0.0654479332402757, 0.05695294487298275, 0.06674542791490222, 0.05413538422786142, 0.05190094004932483, 0.07347053950199482, 0.06397286204956319, 0.05125239715590736, 0.04203579603888335, 0.03977339974004739, 0.12517362838368382, 0.1426472562135678, 0.08479200814989755, 0.10925895499576133, 0.09007835492869253, 0.040639027963550435, 0.07912345129858393, 0.11608019340878908, 0.03693253934775829, 0.05063916820015091, 0.07383269873362253, 0.1317586950742438, 0.07814422462093262, 0.10818876188259678, 0.08665105452988395, 0.05616858301162855, 0.09035073365565323, 0.1371477265185905, 0.0834669175552555, 0.10494876411565639, 0.0639494330067938, 0.08205456233571602, 0.13343443335540955, 0.10350679970424913, 0.06619943746208919, 0.04815256761860936, 0.07784528428006565, 0.06292250987778104, 0.10077309976183993, 0.06719459242930381, 0.05157918152970536, 0.049562772236008544, 0.04315546810667522, 0.049026037865477184, 0.10606941727990161, 0.04072844790046169, 0.13458731418110018, 0.07072538975322454, 0.1294391169850473, 0.02761163199761126, 0.05335374138938373, 0.08935246094178097, 0.0527304991670277, 0.07893201310043414, 0.0727450847447469, 0.06786696687656225, 0.07408225316722306, 0.07938377444834092, 0.11176341054867418, 0.06307986118996076, 0.039606555305291336, 0.03799131292203103, 0.048702979884068305, 0.04237714665531503, 0.04926653652324618, 0.037353768887839506, 0.031868367580551706, 0.1299479589998662, 0.09453129693819173, 0.03350680498167688, 0.05916298756342283, 0.18741730885822072, 0.06367620281565273, 0.02932743617352149, 0.04273328370458754, 0.06732652540467353, 0.027971349146243624, 0.0617930459860611, 0.10158453219873016, 0.1703630666586785, 0.09557271348163693, 0.055574686179138605, 0.02521188433837155, 0.056511994715291516, 0.1121421489697785, 0.023751730326383093, 0.1393814599850494, 0.03862766513787592, 0.030340794789004942, 0.0941023787209487, 0.09737689993383497, 0.027014509542745074, 0.11802053132232503, 0.07845053612973417, 0.10346907470606267, 0.0718337016334502, 0.050088015224373686, 0.037064764487054855, 0.04680941362966736, 0.04791841745657094, 0.188926803280777, 0.07886505678070185, 0.11932513983034024, 0.037739899629509535, 0.051352415613875074, 0.09041236506910455, 0.06274301196828654, 0.17646744212970372, 0.1644910558784788, 0.16655322126225, 0.11531855296194807, 0.04136192127921565, 0.1100725177973477, 0.056111330803809145, 0.12677530734691814, 0.04726832196205862, 0.04545340606944894, 0.04130149624504671, 0.05416416495147975, 0.053675216444571607, 0.045026086648474344, 0.037770838267192144, 0.03703818624641033, 0.029737756499311728, 0.09081645130983879, 0.1713752680166064, 0.036208455815221245, 0.03426142696965996, 0.07169800368530634, 0.0389201384691808, 0.10098829449408674, 0.07746921241286137, 0.1572902511518514, 0.028113227560663215, 0.03765237419114809, 0.029992335626482423, 0.1643019033111565, 0.12424253203042798, 0.01981562282067018, 0.02237726151032283, 0.03292780270713326, 0.18051142178814394, 0.0247643138695927, 0.032949769375644235, 0.18173392172775832, 0.015642530172011775, 0.0734215783357773, 0.08749470444488869, 0.10285368214955207, 0.21759724596433772, 0.010906723409905745, 0.013646228654118256, 0.1297014146554429, 0.1307577404926073, 0.03327348033333392, 0.05485672186092041, 0.03608559248935127, 0.03788767394986858, 0.09516155590641977, 0.12463637370765347, 0.05008462183857559, 0.18351086530283642, 0.04127238080350344, 0.16714520604610303, 0.09741576161215158, 0.10139168309458425, 0.04087576762758773, 0.07634985769396851, 0.0646555050854876, 0.045065714163527525, 0.19232028613738641, 0.11401067812849923, 0.035719731883669455, 0.1098944237713605, 0.040975804891966665, 0.1301551262393291, 0.1316775360848338, 0.048202008960018194, 0.05398493440688106, 0.04017638262796409, 0.04805707881549089, 0.04810357534006452, 0.05092807078516484, 0.05556736656423023, 0.06442921698441183, 0.03831039052415672, 0.0943747271470355, 0.04188341505370958, 0.04824565355955373, 0.05470057936564064, 0.13977596588049046, 0.142609386313129, 0.044325370407775046, 0.04344014965601131, 0.040931378666716554, 0.04237339122604955, 0.08598589144327086, 0.14457085443760018, 0.10549113165734984, 0.13298990460001084, 0.09352472244642235, 0.030783528844251774, 0.10814548234651834, 0.08964794326966236, 0.13881712598227047, 0.08836335595642979, 0.03915378288258299, 0.10301202835195897, 0.12158677537445589, 0.06831800111298872, 0.07969131836510311, 0.08372897905185765, 0.12008467469938161, 0.060141287752609955, 0.07356798139689388, 0.07612316859509828, 0.11626576343661757, 0.08310236116151516, 0.07481518418589825, 0.12025501861049782, 0.08486032048291538, 0.08032719820381867, 0.07234079977062488, 0.06562633280142348, 0.11447204019111068, 0.08398882091786086, 0.08889149543898998, 0.0810727193450045, 0.052986485521153856, 0.06059991898535817, 0.0654786039617191, 0.09782815617993554, 0.06564920542057229, 0.05734258361360479, 0.09291055315989252, 0.07533482608180452, 0.06715604654904758, 0.10834151807251836, 0.1234048829887149, 0.0985218191005807, 0.0727441721641222, 0.08967498257932911, 0.1019129661896536, 0.0520360813505303, 0.05829273646654289, 0.10716861404580047, 0.09403761425709005, 0.0655707139415095, 0.08143347351131089, 0.0766741836445159, 0.12894895091386896, 0.08970303761597928, 0.07747264477554451, 0.07229844089352418, 0.11573598366727805, 0.11542970468880473, 0.08471632554283565, 0.07370327471436453, 0.10207366368012222, 0.0888687907216552, 0.08452144452939397, 0.09236382947854606, 0.07567190042555384, 0.06343114348789049, 0.05496649066805483, 0.09664256813715869, 0.09364122012594442, 0.10402885812373337, 0.06319484322800029, 0.09725279417429782, 0.07583107108970687, 0.04760483353319233, 0.045122196231862616, 0.08653788749669285, 0.09460913897773955, 0.10147338528458377, 0.10819743955993699, 0.09474437883501838, 0.09061091927223719, 0.10184273105194032, 0.06286300437196539, 0.06288650660699067, 0.0497162604715173, 0.05136459012116586, 0.06640648840193135, 0.05402354104942501, 0.050795275535449214]
jsd_equ = [0.008748994684134268, 0.015240537320908422, 0.0015240513988232995, 0.0031051148679070014, 0.0033735233256568784, 0.002421185881730095, 0.0036073414352532987, 0.003849237851658265, 0.010703146709061117, 0.001975003412196996, 0.0032388009910297787, 0.0033171020847916253, 0.0022375245606253186, 0.008835788288123213, 0.002251804174186225, 0.012975544998831311, 0.0029251502647842263, 0.003520611946407365, 0.0027328098662684546, 0.004669021702278735, 0.004389173710159215, 0.0052263420164222665, 0.00925964078586519, 0.0019185349128100077, 0.003406742393244508, 0.0026002231282451225, 0.003045507093689207, 0.0067725270507850675, 0.004615923237517347, 0.009494840581165086, 0.0046539826922372025, 0.0029901092897060464, 0.0015919472396219618, 0.002341132882329799, 0.008668640534694039, 0.002719877015996795, 0.005893563638018638, 0.0023407478450889006, 0.0010666309765906018, 0.003181317882297267, 0.0008688960500944033, 0.0018644504769192028, 0.002971659222288935, 0.007900296035128162, 0.000539324172271058, 0.002070575204687525, 0.002406317190937706, 0.0025697463695358285, 0.007139095707732642, 0.004222044168417817, 0.007282998170726579, 0.011216860395627186, 0.008315359831170488, 0.004959953982169934, 0.0076942042005910555, 0.002873583360384834, 0.01007298973427609, 0.18211119159482825, 0.0531437787736118, 0.020538666252942844, 0.008202611396243096, 0.013486987254674272, 0.007025516692222527, 0.007968103980006257, 0.00565440793585731, 0.007850874676782024, 0.006883947056933503, 0.004533591600688811, 0.0074019467571685696, 0.007666759799457192, 0.0020304089373184312, 0.008168592036003026, 0.006297009040415333, 0.006545417318380353, 0.004279373035834545, 0.005463314780357911, 0.009132897705699949, 0.0012589590299461146, 0.003077497457671197, 0.007169884482741821, 0.006497335566025242, 0.005035924853373506, 0.005213834137590346, 0.010163536422927676, 0.0034621070971155832, 0.004928462153098465, 0.003895404550470798, 0.0029072073566535858, 0.003232659843453966, 0.003840357774316221, 0.01275522124106924, 0.001988635570324742, 0.011946891346651492, 0.001629165340951174, 0.0022818483445895647, 0.003944023254344372, 0.0024269528836270747, 0.006704720069243376, 0.0017179430545035484, 0.0068923543406214085, 0.0024687533177489215, 0.0021391592684809183, 0.003337229812832167, 0.003418460009092912, 0.00963774241925934, 0.0019908227765451374, 0.0085369465407919, 0.0022313013645565757, 0.0026349226184029582, 0.001866284445646571, 0.00453337010184295, 0.007959710325099978, 0.004286140741141147, 0.006479426746063331, 0.0070482861398849465, 0.003513510351339872, 0.004011216177183012, 0.0022158782594764465, 0.008482467574922936, 0.0018005973868901156, 0.006927645000266355, 0.0031788619299485516, 0.002827146060151168, 0.0027326713259520825, 0.0023513370068489726, 0.0034413868280844797, 0.0029409963734202743, 0.007653961969824965, 0.002333952196163844, 0.0011181270942302469, 0.0029508407614112046, 0.0021271743015999767, 0.004425760886956154, 0.002168421836833714, 0.012305351340361502, 0.0026827322564296416, 0.0019098908469046747, 0.0013592964300862566, 0.002380318485733921, 0.008394673464354855, 0.004556734738429836, 0.004469325735883187, 0.01574408344673982, 0.0019610301160683423, 0.0023490759532661027, 0.0037439040817400598, 0.006537844089600558, 0.00502209584745454, 0.00865884774549225, 0.003428085636320212, 0.0037721336253018815, 0.0022381926818572967, 0.0024972709191267745, 0.003696137837246074, 0.001495232459583108, 0.02259290285903107, 0.004747108468096055, 0.002821409752301705, 0.0016619797877835908, 0.0018547106975043703, 0.0030819951024492207, 0.0026091704366595545, 0.010266012627590158, 0.0028516783112439176, 0.0021412014560428243, 0.0033114344234404396, 0.001540835573547622, 0.00421042657083937, 0.001609677677026934, 0.010826776678340588, 0.003281086486635346, 0.003104976013677881, 0.0007294907035820844, 0.0013730124485286691, 0.0029796799855134745, 0.0033320783291904826, 0.006138875297775175, 0.0025269100477785253, 0.0018474482619564604, 0.006550181258772119, 0.006058177303177359, 0.003684488058162373, 0.0060383056125407585, 0.001998049651805986, 0.002513968582648026, 0.0038666068174424218, 0.014656122879418133, 0.011672860109471581, 0.006142586502766021, 0.0012173613424367746, 0.008857786961960937, 0.00385930985089498, 0.0034151708501511517, 0.005681893168830065, 0.00295904086741758, 0.0030945633988773064, 0.0025890161030214746, 0.00931731631094925, 0.0037796954562716407, 0.0024056415775821766, 0.0030189537084744393, 0.0024941422590980594, 0.0011302871904916953, 0.010338659020832449, 0.006384228024171711, 0.003107964928195201, 0.0030667869682372345, 0.0018064458231381573, 0.0023188327254547135, 0.006614682180564619, 0.0018241886947836265, 0.006805696163668241, 0.002559666832954304, 0.0025331049125342855, 0.0013611815815298394, 0.0002709540976480625, 0.0037241045005423764, 0.002376689343175004, 0.005225119164560578, 0.0012506956192081915, 0.01716175878580618, 0.004205132960958305, 0.003507711986412852, 0.009337160353107955, 0.003040117972305669, 0.002585514316955118, 0.002260336278832566, 0.0032094571197341334, 0.001460078946165939, 0.002736534340808948, 0.004419932719028959, 0.002733579737080539, 0.003587940703536317, 0.0016956952378995283, 0.005479556283897656, 0.0049320044354873235, 0.0015502869119702334, 0.010463913315544278, 0.003112910633934105, 0.0033806295197996283, 0.0027050788380969656, 0.0006166887812586972, 0.004075737582778353, 0.004530107416332196, 0.011411086147895688, 0.0015218294398832875, 0.0014176485128186052, 0.010083405442320186, 0.02365760149932455, 0.007721393362194236, 0.004868469935865827, 0.001116444356297833, 0.0024494117120294695, 0.0035745596680197096, 0.0021758238903891924, 0.0008367696176108553, 0.004703960603485181, 0.00287994622794217, 0.005897651935413488, 0.0022638294050707983, 0.0022425480930810737, 0.002010716636285551, 0.005485271402202439, 0.003923292536136854, 0.006514403929646487, 0.008280239501136408, 0.005168807505326366, 0.0024593596638259247, 0.0022910004466175343, 0.006632987130707922, 0.004132152533710266, 0.003218792726717057, 0.0026595223518779596, 0.004934047877792711, 0.0024624531209616607, 0.0025901914492929908, 0.002044777073571057, 0.005291756204156415, 0.003121458484824457, 0.006711224585810493, 0.002433222565360869, 0.0036495174298812956, 0.0014424453300211587, 0.0007164052802857296, 0.0043769117936971825, 0.00879621822274281, 0.007835843150318841, 0.004673343037982561, 0.003995782704419247, 0.002761337379385999, 0.0042885507731858724, 0.005233338118323313, 0.0037584392854631424, 0.005524618964267186, 0.004899969155736111]

jsd2 = [0.10912704201369046, 0.19845387518896526, 0.06636123715181373, 0.22965979334604705, 0.10251125593795132, 0.08666620434894592, 0.07927349706682171, 0.19848447080357445, 0.14599751556934792, 0.1383789007638873, 0.05738839283228865, 0.14050797661721287, 0.08346897797106193, 0.11916504252332372, 0.14463674072422486, 0.25292511118834515, 0.12044171545059677, 0.12918598734212278, 0.09051850752800643, 0.08520046766556473, 0.1386281736624549, 0.17080101247304907, 0.17381182466514866, 0.06025850160523811, 0.09440916452556755, 0.08082750033623852, 0.08510413359880713, 0.09033872431467743, 0.20955023976101889, 0.2009557695097311, 0.07592308418331008, 0.12676263470223936, 0.13335200993684307, 0.08285188968515632, 0.18012434155247858, 0.21519241495131336, 0.2473740524175701, 0.08228627176558284, 0.08687884813927899, 0.06270549307775242, 0.07088959738119995, 0.11513748902758086, 0.20149280531872085, 0.19530319464396936, 0.09253449387233231, 0.14060697895018176, 0.07791141447630034, 0.14352385321184036, 0.11686241585141288, 0.20433317474356233, 0.15052584467232544, 0.05962915617434022, 0.11935219312179524, 0.13366841238171773, 0.17362710564158151, 0.17715230910960714, 0.23236721781729797, 0.17130903246920803, 0.13159086274028584, 0.14827753018554238, 0.17165885082686905, 0.116133503784391, 0.1278074842790888, 0.07705680324429542, 0.10726812780852865, 0.08805573187622007, 0.0727482082907239, 0.12725644223561092, 0.08192395427645693, 0.05552018254137901, 0.1780827663494532, 0.2927071222462903, 0.127987900397496, 0.13015487852327054, 0.08964708861651065, 0.11038870967776224, 0.11140966401069669, 0.22586803380872453, 0.24238635797931052, 0.1412869198407523, 0.08578225862674058, 0.061907320621412014, 0.05712386400783202, 0.09559475313500998, 0.15712572802893768, 0.2437041640515502, 0.0909076859150842, 0.11245895331714992, 0.08169221969754134, 0.13558715241470923, 0.2053903535475605, 0.2412527502534124, 0.23259438123589743, 0.15152273963321583, 0.07484526398075339, 0.16463862534819185, 0.22200386497230462, 0.13144249745614264, 0.2030909848783401, 0.20446920166662177, 0.07677468697443617, 0.10312828715564726, 0.0868905830496055, 0.14427369502099352, 0.15582291834608564, 0.24190440507080063, 0.3863017659378454, 0.12104047802783713, 0.13252862610269167, 0.1153843505105928, 0.14120668811589843, 0.20264574080661069, 0.19377933549939783, 0.2888000146796105, 0.30250332938509894, 0.14925865419116927, 0.06793076243230424, 0.17535971404257208, 0.1353063513841383, 0.27103336294794406, 0.28347752294571, 0.136765440004599, 0.08845396297357484, 0.1625942965846969, 0.14345944793169035, 0.13349281622579992, 0.22836928628922865, 0.32460394132662096, 0.14470890559551483, 0.16504306357400444, 0.11018502405176979, 0.14777005874217744, 0.12284843359657996, 0.27383697957593056, 0.3785244359579088, 0.1703112444085024, 0.132352539026377, 0.08286246777645952, 0.14580073404263327, 0.151501085249494, 0.3029907103787684, 0.2103548767441808, 0.19806659397389026, 0.1559974798558544, 0.1225993866244568, 0.10582041320406399, 0.12320523664954036, 0.24782121950093833, 0.33545538903707783, 0.11186297446734064, 0.11670714635064339, 0.09208098868396275, 0.09864024821251839, 0.1904180167284184, 0.27359035276024285, 0.27167202774897603, 0.07234162705304638, 0.07045931060317726, 0.106894062512355, 0.11731347941970902, 0.10813763679608591, 0.2649296499576491, 0.37241493038075113, 0.15605613534590285, 0.11852161078886403, 0.17248802930459517, 0.0816050475560673, 0.1223498836740754, 0.25153284992268204, 0.3251496605747272, 0.10742817510444172, 0.12496006176469776, 0.12568312614430174, 0.1138789133770226, 0.09704136379914446, 0.31680382218116626, 0.3119840583122243, 0.07324965732451368, 0.07094723146019187, 0.18512915323734658, 0.27715429608540076, 0.18259353683313279, 0.19502218897202003, 0.10823708876654581, 0.059590835181879846, 0.10404589593558453, 0.43381793144934533, 0.36297775068750726, 0.2009318270275655, 0.2922269711053988, 0.32695522223217194, 0.22060776039841337, 0.08467770339688332, 0.09846566618202676, 0.1425994813159664, 0.10560759977167883, 0.2491018082180622, 0.30582764765491344, 0.09242140212650243, 0.10881780893671461, 0.15466565778015093, 0.11414480158725332, 0.07111935833122018, 0.2108598578590975, 0.3447076431947429, 0.15355965048322287, 0.11963295475932872, 0.1146122238312386, 0.14825919104608953, 0.1592534364360512, 0.3618075584157287, 0.36951418866536484, 0.15890643250282174, 0.1496804367976688, 0.1382130648087098, 0.1478266691602334, 0.1856226148335205, 0.32470727024016377, 0.3298667420128184, 0.13576017880770394, 0.17664012085468758, 0.14953451241844123, 0.30679786398554393, 0.3037995907043724, 0.11244232761331324, 0.144777619728559, 0.10398065008524379, 0.16739300757541753, 0.14340723851033726, 0.28903162038439595, 0.3435341803325192, 0.16334452298992122, 0.13996812312971393, 0.21422970774678807, 0.16332128534231094, 0.14699515129888532, 0.30255473298907887, 0.3688225859258313, 0.16889074741947557, 0.13082051156181232, 0.09574401341629205, 0.16472291502808661, 0.14536334984296537, 0.26572975846586716, 0.2988310456381852, 0.13089380988264132, 0.08342568968651426, 0.1324681072231177, 0.2685008327166479, 0.23844969599996946, 0.21460011497261008, 0.23174465207762845, 0.07737407359285518, 0.11154816760080444, 0.0933788784292503, 0.0744707671433552, 0.09691838023609016, 0.26734515198288133, 0.2510045136904841, 0.1061606410780436, 0.08448067755108604, 0.061679338523226046, 0.11480607511896104, 0.07848439839909188, 0.26122240015130643, 0.18179929750736845, 0.14489199167494476, 0.07034397855438923, 0.1409722461297232, 0.14382464132013043, 0.16653202143535062, 0.180404745470255, 0.20844735676452886, 0.12954983545208845, 0.10237583133703375, 0.11401385302719771, 0.05168237553626681, 0.0568750510297617, 0.246422670725448, 0.26857625768571075, 0.1048306713580753, 0.08621447807028725, 0.08251376114942252, 0.08204491034477712, 0.09582152346219694, 0.19359005622261777, 0.26409240888860125, 0.10144031595648723, 0.06287031841094017, 0.10716735641381211, 0.0736293282194725, 0.1294230381058224, 0.25860054052730397, 0.27774714952582347, 0.11851798226626231]
jsd_cen2 = [0.32256760379361726, 0.3810239639317933, 0.28386663245410493, 0.35230754830673466, 0.28189384029941755, 0.2990176428977388, 0.24311679125495256, 0.3692207262558338, 0.34815422147146746, 0.3086180294974303, 0.2190867719629146, 0.2944877706533938, 0.23662774226146438, 0.3309871042516204, 0.43175927961812877, 0.35225026853698854, 0.3506640374165292, 0.25018682290870126, 0.2018944636423843, 0.19958628735050707, 0.2511881602458358, 0.21825640670517163, 0.3277881493146352, 0.23731398417432872, 0.2651893172458749, 0.25987672849498034, 0.1981169965350415, 0.3305360563766058, 0.3013549901242266, 0.28440338403422183, 0.28229077822524445, 0.24597592507096025, 0.2689289289249557, 0.26723613384157013, 0.26051423720450034, 0.4598711221548436, 0.29199940349935083, 0.2251773592006137, 0.22380082229940482, 0.2459725847967571, 0.32849376864464885, 0.1908232890968055, 0.31989906513324307, 0.32991462184432313, 0.31619989409047616, 0.29599589101452783, 0.33142278114623064, 0.2800054579791898, 0.3281902150886128, 0.3242061842283341, 0.28508548123760513, 0.3165442627196493, 0.29439248623540115, 0.280880018188317, 0.4402812786150543, 0.22841474211560983, 0.3752587645937397, 0.250537545003473, 0.236924835544984, 0.143041665652949, 0.19756006910399015, 0.20170043820336014, 0.22989958013678133, 0.20357673808875332, 0.2823378671559504, 0.3020928363649714, 0.18589749572654715, 0.31343670974684334, 0.2337374009942335, 0.30641242467725643, 0.31438688575758694, 0.3663003586378917, 0.26690527231045974, 0.290334571377121, 0.27951540668418196, 0.24195819156521706, 0.2637679765623775, 0.2926738393659329, 0.2649750293539159, 0.2541129910728474, 0.23056036822725479, 0.2420132797701976, 0.26567316524371415, 0.2340119173868865, 0.2763747331629617, 0.34789842920122444, 0.26551206992806975, 0.2970711176190934, 0.2785566291322321, 0.2586713412063521, 0.2996400865965023, 0.25534217370222645, 0.32990086267971536, 0.29399145490637413, 0.2231244809511516, 0.22476818018443814, 0.2606277227700641, 0.2993480878714107, 0.40823548802564064, 0.2993049504345083, 0.2532845811947855, 0.23632946589625708, 0.22561061571619265, 0.2585084890570179, 0.27496667886026543, 0.34172372884629465, 0.4059531282917037, 0.25352943850494, 0.2639042273798796, 0.23665775368308165, 0.24748167113431271, 0.3326341415880758, 0.2725645770366945, 0.4392141997475013, 0.4038023356470809, 0.31048750569369093, 0.24348218113665898, 0.384957098822698, 0.33032023010436645, 0.39303588336177686, 0.48263021642916587, 0.3273285038788882, 0.2373557612566947, 0.33587912337426745, 0.3279458145263568, 0.32961870580003944, 0.32353058572707105, 0.29723614664558573, 0.314573773306344, 0.31546491847300967, 0.2546415492172548, 0.37148036131721385, 0.23773918371790997, 0.483608525101617, 0.37377921589995683, 0.3306034234805854, 0.228728127251514, 0.3060731607994856, 0.2510985946654703, 0.3690531657477507, 0.48782489985381505, 0.3251017352797856, 0.26441317351661925, 0.2735457534362614, 0.32083136906053794, 0.2067776662610242, 0.29932876614239395, 0.3100787206291962, 0.3381825833124489, 0.2873070340995373, 0.2809097066239348, 0.32539989065975544, 0.31901835486820374, 0.36810034229848837, 0.461279311850522, 0.3406900370976521, 0.2977669304371506, 0.38888332935823733, 0.30163929829236397, 0.29795014449340895, 0.3143293142079014, 0.3222078225414255, 0.3479932555176853, 0.2838459039025052, 0.3341721608967952, 0.2673677936147819, 0.21576624497159247, 0.19787098832416017, 0.3454374281763313, 0.5635162595610991, 0.3175222542149238, 0.23327153989203436, 0.3631600106142736, 0.3247156474357096, 0.2783977351364343, 0.2911053203552527, 0.34275769077547374, 0.22744354490629837, 0.36013222144095014, 0.20948668052905065, 0.3490101520797106, 0.41389517210567184, 0.313593195465691, 0.3012626209382832, 0.31509841250581744, 0.2958460720663987, 0.5297636379708939, 0.41831460110854335, 0.37340140825840457, 0.3183886070524964, 0.38578593409197104, 0.3568503201898679, 0.3289843233979286, 0.30033804498720884, 0.3666466847867731, 0.27756569556938576, 0.36339049102974913, 0.4251994186020227, 0.3027721698113297, 0.3432652186084481, 0.36845071579378386, 0.37238149854872704, 0.3828050065781248, 0.40299903562047024, 0.5564011823707898, 0.2546924278653652, 0.2205511567569662, 0.1767057223379845, 0.29518084919190135, 0.41524649597051033, 0.3283295718269389, 0.3681194592514805, 0.2642276396277244, 0.27141927853413195, 0.42043249221226237, 0.2894266103737201, 0.2582858882615837, 0.5309061219680031, 0.5183395148725904, 0.4006075957329193, 0.31241473152230265, 0.36309527715722206, 0.4882660275022516, 0.33616259335970533, 0.39875086456595465, 0.30440144361516097, 0.2763511866235112, 0.37371429068742096, 0.31122460439057276, 0.35103154556098853, 0.3577897417910386, 0.31312545702539646, 0.39897657071109377, 0.3754132364682261, 0.3773481395763152, 0.23687416874791586, 0.3706289330792578, 0.4002461702801223, 0.35419504022933007, 0.3194552245142296, 0.33141371689164567, 0.2591929616454366, 0.39632908392269, 0.4791624005098857, 0.34845325473738253, 0.29658485578957733, 0.38948840867675677, 0.23186295756447142, 0.38467785886427347, 0.36856270830170096, 0.41997928590830397, 0.3247579083704727, 0.19648649613989505, 0.2023672585617845, 0.3277978859848206, 0.2619796590776307, 0.29527056163367327, 0.4784870294746472, 0.49238400870611476, 0.35266179872696435, 0.22205542305373435, 0.2591346092999909, 0.30574588602361186, 0.2650286061401144, 0.3733281490372477, 0.416496182634096, 0.4308051745897152, 0.30864638725476756, 0.24836471629906953, 0.2845769387907223, 0.4580807290515381, 0.31843374833239024, 0.3398212999103301, 0.2867163124246657, 0.30517953181727175, 0.3600599324890424, 0.3998232709171424, 0.3523954929530551, 0.4195980979325788, 0.4678805517495335, 0.2851894156376524, 0.2867093903393213, 0.23387409676311982, 0.2058880416973707, 0.24080934637100154, 0.3151224434372673, 0.39410112509381173, 0.25048108135699526, 0.2903540681717152, 0.2060449267844759, 0.3344124392878762, 0.31623423941184114, 0.5299252671743316, 0.46384824860924007, 0.3811719815869311]
jsd_equ2 = [0.25842873559530816, 0.48805067009499936, 0.25709300494484005, 0.3148173862245477, 0.20924494184472245, 0.17588695388308817, 0.20951954662560437, 0.40259313296914034, 0.3540844194287478, 0.30757800432596183, 0.23314389942701025, 0.25327278933190916, 0.2705237067073031, 0.2779122560416565, 0.3534049762040451, 0.4577256154564847, 0.241953259847496, 0.23371382333689433, 0.24486434745442245, 0.249291896176284, 0.39828936740058685, 0.3673163147504946, 0.4062098983270415, 0.1834192815051894, 0.19951892560493284, 0.19300366917992406, 0.1939169905283136, 0.2414498886379698, 0.3708552177235844, 0.4660819680838776, 0.16942540473491288, 0.20919778912853226, 0.23178339977027057, 0.16729551794359704, 0.22482996648506684, 0.411537882266304, 0.38215703482017355, 0.22758541058067308, 0.21834207073141854, 0.24712169876683793, 0.15712840100491968, 0.25231038738511946, 0.42201068704056505, 0.37323047815516003, 0.27818772673444897, 0.27626001588117494, 0.24904246577552572, 0.30761498728564585, 0.2730578401038962, 0.3695121977312557, 0.37418626487959344, 0.34955325278631144, 0.34462504130749344, 0.3424846309632886, 0.36005938969390816, 0.3591788629326745, 0.41686961037059983, 0.3875827841505475, 0.14009411093018131, 0.09396016131990524, 0.11425968223847943, 0.10997459502196556, 0.1577862213042825, 0.18267281172568192, 0.3057989180528729, 0.17700004808967856, 0.13939771621467714, 0.19535369339044, 0.21960728587211967, 0.21470901061514197, 0.35995032731305626, 0.4710509420027055, 0.3328126319812385, 0.2528616131200826, 0.2881429299765599, 0.24283027974523613, 0.23558483766211694, 0.3750282374009799, 0.42434724240660654, 0.24234147899906106, 0.2316723975894018, 0.16799544319490367, 0.16188098275526935, 0.19960133588538528, 0.38403222074020743, 0.4130408182103107, 0.2278312300331575, 0.28023567537377714, 0.23507978094325455, 0.18274109568979294, 0.264117870682982, 0.3875522396673211, 0.3836809704596461, 0.2807329562097677, 0.2474256010015049, 0.2921346804779669, 0.4076738285426918, 0.2841237962740574, 0.3959424823146697, 0.39547399216647255, 0.20845930595540713, 0.1853598492150155, 0.23248041893793198, 0.2314659950164859, 0.29057029529865347, 0.44057944276511585, 0.5053710599399757, 0.26524750391468865, 0.22115047725415787, 0.2444708342160002, 0.24491961355395128, 0.2801375467874707, 0.4051691437037655, 0.4112906010411874, 0.41701437878092656, 0.2604753951885367, 0.27228867521520855, 0.309041841634347, 0.29310180867622304, 0.4345864351911541, 0.4294402016650377, 0.2186120371312063, 0.250684296143662, 0.2517556646737932, 0.21203845612041905, 0.23220722157389184, 0.40564024167235335, 0.5032155337924489, 0.28807863684125723, 0.3318069301758309, 0.2613678830953727, 0.28980618404651015, 0.24406132805339453, 0.43907030693459065, 0.4753694294255599, 0.2757210431763112, 0.2813276273975618, 0.24652397957827915, 0.258113719366411, 0.2786468906105526, 0.4327330146911007, 0.43961783329947796, 0.3974343514806759, 0.3167839863517189, 0.3217825861765987, 0.26235556024266404, 0.26333867001476263, 0.4338137502093032, 0.445473191798162, 0.26103107831008976, 0.25227780815406525, 0.2922842782843797, 0.23274997773723108, 0.34970046146677614, 0.39848821249802346, 0.43596789161676597, 0.2994253566058135, 0.27465137207612017, 0.29541314255845263, 0.2438373262581261, 0.27389176052791125, 0.4542056088597296, 0.4837022902645041, 0.32728441438342754, 0.2990354889678587, 0.3082202173342408, 0.25578871202845116, 0.31137758891882544, 0.47790136660176613, 0.4776168006161909, 0.2586452545455152, 0.2665714972785343, 0.3706201535632875, 0.29326037773352137, 0.23484184078010228, 0.4516967530844854, 0.474510772094062, 0.25536964486050673, 0.27443745372804645, 0.2957570302934817, 0.4907403050539318, 0.44608686045721063, 0.4395363956659567, 0.37300683635313736, 0.3134522126340619, 0.2848102363739001, 0.611046183655433, 0.5334576963239014, 0.32949790438302146, 0.4672799531724751, 0.4805115982715944, 0.34030931911582935, 0.3430072559452186, 0.27979647697181753, 0.31218803423094454, 0.29338908325137575, 0.44261317771977277, 0.499271935553576, 0.26292320335757585, 0.30503113799369636, 0.3136031053658368, 0.348770569979263, 0.33428346244073925, 0.45244612386469174, 0.47451077209406195, 0.37573562992033294, 0.3480813343355233, 0.34018399348021755, 0.43216841203059037, 0.35640254278061073, 0.4847920934922871, 0.47553873108935957, 0.39340405550189356, 0.3546645488801481, 0.34812990019219353, 0.35799719334278807, 0.3819443076942334, 0.4681814174080386, 0.4781149103178488, 0.3791423772359014, 0.432534424642914, 0.3277253655945546, 0.48608566536083414, 0.49645417340142944, 0.3252147263384662, 0.32186420659428794, 0.3399460343281493, 0.3503776045304529, 0.4194205511682905, 0.4725827641875835, 0.4810097079732523, 0.38117892363660855, 0.37695376769404554, 0.41283887440806416, 0.3518642413755729, 0.3487395050393055, 0.4860411060815762, 0.5335144228914166, 0.3424186666316232, 0.3228587786952256, 0.2952717012547525, 0.35253284968008924, 0.30841396352183337, 0.4729176016438354, 0.49331648428242103, 0.4150623183922661, 0.34381573130539417, 0.3253496573970535, 0.49614427148892254, 0.4679621671453208, 0.4674727573046344, 0.36752756964724254, 0.23740553957941715, 0.3078433474191715, 0.25991061534051774, 0.28365983758677105, 0.2921462858832754, 0.45955764478229844, 0.4418791555963856, 0.27108250533987865, 0.27820217474489894, 0.3172594803599287, 0.3423100510722035, 0.3413361486458485, 0.5050152153498225, 0.44003481571309533, 0.43770295537306225, 0.3499833218679646, 0.3353627417084397, 0.3888952590097007, 0.4458519918617043, 0.3657795115131028, 0.35446923184794277, 0.3059792115495906, 0.32232373033377126, 0.3103449616352383, 0.30187029172451424, 0.30430454645626137, 0.4433453544449006, 0.5115535418220831, 0.3047516340121733, 0.33452312280436014, 0.24696698137450224, 0.2496664668584581, 0.2960509997082713, 0.44665117903573415, 0.4643764354413655, 0.2858699190680331, 0.26321841723010286, 0.21907041302445673, 0.3180495367151949, 0.30799487830231986, 0.46838460278922994, 0.46309977715801176, 0.3496172562403488]

figure = plt.figure(figsize=(9, 4), dpi=100)
# plt.plot(jsd2, [1] * len(jsd), 'r.')
# plt.plot(jsd_cen2, [1.5] * len(jsd_cen), 'b.')
# plt.plot(jsd_equ2, [0.5] * len(jsd_equ), 'g.')
# plt.yticks((0.5, 1, 1.5), ("Equalized", "Normal", "Centralized"))
# plt.xlabel("JSD")

data = jsd2
sigma = statistics.stdev(data)
step = 0.5 * sigma * (len(data) ** -0.2)
dropped, dist = Divergence.histogram(data, step)

x = []
y = []
for item in dist.keys():
    x += [item]
    y += [dist[item]]

plt.bar(x, y)
#plt.xlim(0, math.log(2) / step)

figure.savefig("JSD-Dist.png")
