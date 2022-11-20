""" module test_telechargement 
test unitaire de la classe Telechargement
auteurs: Jean-Philippe Trotta et Chloé Contant
date : 20/11/2022
"""
from client.telechargement import Telechargement

import unittest

class TelechargementTest(unittest.TestCase):
    
    def test_generator_link(self):
        '''test de la méthode qui recupère url'''
        
        t1 = Telechargement(id_zone1="08",date="latest",zonage1="departements")
        lien_1 = t1.generator_link()
        test1= lien_1 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/departements/08/cadastre-08-communes.json.gz"
        
        t2 = Telechargement(id_zone1="08124",date="latest",zonage1="communes")
        lien_2 = t2.generator_link()
        test2 = lien_2 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/08/08124/cadastre-08124-communes.json.gz"
        

        t3= Telechargement(id_zone1="08",date="latest",zonage1="france",zonage2="communes")
        lien_3 = t3.generator_link()
        test3 = lien_3 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        
        test = test1 and test2 and test3 
        self.assertEqual(test, True)

    def test_generator_path(self):
        '''test pour le générateur de chemin'''
        t4 = Telechargement(id_zone1="04004",zonage1="communes")
        test4 = t4.generator_path() == "Application/client/data/communes/communes"
        self.assertEqual(test4, True)
    
    def test_download(self):
        '''test pour le téléchargement du fichier json.gz'''
        t5 = Telechargement(id_zone1="07003",zonage1="communes",zonage2="parcelles")
        test5 = t5.download() == None
        self.assertEqual(test5, True)
    
    def test_read_json(self):
        '''test pour la lecture du fichier json.gz'''
        t6 = Telechargement(id_zone1="07003",zonage1="communes",zonage2="parcelles")
        t6.download()
        dico = t6.read_json()
        test6 = print(dico) == {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'id': '07003', 'geometry': {'type': 'MultiPolygon', 'coordinates': 
        [[[[4.32867, 44.6983452], [4.328674, 44.6983798], [4.3286598, 44.6985433], [4.3286249, 44.6986959], [4.3285857, 44.6988481], [4.3285689, 44.6989084], [4.3285601, 44.6989692], [4.3285121, 44.6993171], [4.3284731, 44.6994642], [4.3284395, 44.6996628], [4.3283776, 44.7000739], [4.3283765, 44.7001616], [4.3284611, 44.7002395], [4.3285091, 44.7003103], [4.3285325, 44.7003822], [4.3285576, 44.7005323], [4.3285494, 44.7006937], [4.3285426, 44.7007742], [4.3285181, 44.7008486], [4.3284895, 44.7009225], [4.3284568, 44.7009953], [4.328432, 44.701045], [4.3284382, 44.7010906], [4.3285103, 44.7013027], [4.3285668, 44.701425], [4.3285697, 44.7014582], [4.3289058, 44.7020089], [4.3290573, 44.7023253], [4.32921, 44.7026539], [4.3292515, 44.7027424], [4.3293608, 44.7029442], [4.3294283, 44.7030595], [4.3296398, 44.7033546], [4.3298347, 44.7035623], [4.3301666, 44.7038496], [4.3305078, 44.7039736], [4.3308093, 44.7040989], [4.3309577, 44.7041651], [4.3310518, 44.704259], [4.331168, 44.7044132], [4.3312354, 44.7045995], [4.3313189, 44.7046404], [4.3314249, 44.7046643], [4.3322946, 44.7047654], [4.3325308, 44.7047906], [4.3327708, 44.704798], [4.3328485, 44.7048091], [4.3329271, 44.7048171], [4.3330028, 44.7048218], [4.333192, 44.7048594], [4.3335546, 44.7049893], [4.3336543, 44.7050146], [4.3337415, 44.7050128], [4.3339241, 44.7050055], [4.3340213, 44.7050118], [4.3341088, 44.7050373], [4.3343447, 44.7051376], [4.3354754, 44.7054979], [4.335584, 44.7055409], [4.3358703, 44.7056745], [4.3360353, 44.7057418], [4.3361351, 44.7057678], [4.3366605, 44.7059606], [4.3367269, 44.7059687], [4.3370271, 44.7060778], [4.3371546, 44.706139], [4.3373202, 44.706235], [4.3374017, 44.7062753], [4.3378164, 44.7064598], [4.3378245, 44.7064597], [4.3378645, 44.7064596], [4.3379447, 44.7064593], [4.3380439, 44.7064591], [4.3381576, 44.7064588], [4.3382259, 44.7064534], [4.3382853, 44.7064489], [4.3384062, 44.7064395], [4.3384716, 44.7064086], [4.3386196, 
        44.7063294], [4.3395088, 44.7072694], [4.3398099, 44.7075981], [4.3400627, 44.7079761], [4.3401789, 44.7081294], [4.3401811, 44.7081382], [4.3400066, 44.7081214], [4.3400159, 44.7081356], [4.3402313, 44.7084401], [4.3405381, 44.708895], [4.3408548, 44.7093547], [4.3410827, 44.7096521], [4.3413197, 44.7099681], [4.3415718, 44.7101368], [4.341835, 44.7103878], [4.3451044, 44.7115374], [4.3452504, 44.7115882], [4.3454913, 44.7116723], [4.3463391, 44.7118339], [4.346811, 44.7118794], [4.3468997, 44.711888], [4.3469779, 44.7118955], [4.347629, 44.7118805], [4.3483084, 44.7118644], [4.3485031, 44.7118598], [4.3489596, 44.7118508], [4.349244, 44.711845], [4.3491547, 44.7119979], [4.3487586, 44.7127121], [4.3486553, 44.7128954], [4.3483802, 44.7133891], [4.3475469, 44.7148829], [4.3471924, 44.7156829], [4.3471659, 44.7157733], [4.3469856, 44.7163907], [4.3469328, 44.716431], [4.3466928, 44.7167807], [4.346627, 44.7167671], [4.346609, 44.7167815], [4.3469974, 44.7169853], [4.3471419, 44.717016], [4.3473292, 44.7170241], [4.347395, 44.7170484], [4.3474863, 44.7171571], [4.3475593, 44.7171805], [4.3476474, 44.7171891], [4.3478039, 44.7172558], [4.3479588, 44.7172914], [4.3482249, 44.7174364], [4.3486161, 44.7174089], [4.3487887, 44.7173619], [4.3489799, 44.7172742], [4.3490714, 44.7172555], [4.3492153, 44.7172979], [4.3495608, 44.717447], [4.3496047, 44.7175953], [4.3496581, 44.7176684], [4.3497408, 44.7177145], [4.3498895, 44.7177452], [4.3499439, 44.7177336], [4.3500126, 44.7176597], [4.3500558, 44.7176534], [4.350344, 44.7176853], [4.3504763, 44.7176845], [4.3505534, 44.7176651], [4.3507101, 44.7176478], [4.3508546, 44.7177242], [4.3511885, 44.7178285], [4.3512471, 44.7178467], [4.3515583, 44.7178845], [4.3517414, 44.7178889], [4.3519133, 44.7179068], [4.3521973, 44.7178835], [4.3524903, 44.7180798], [4.352207, 44.7183744], [4.3520805, 44.7185351], [4.3519931, 44.7186937], [4.3518793, 44.7190399], [4.3517619, 44.7192815], [4.3515855, 44.7195576], [4.3513807, 44.7199594], [4.3511976, 44.7202252], [4.3511848, 44.7202439], [4.350918, 44.7201826], [4.3509265, 44.719932], [4.3508773, 44.7199062], [4.3507811, 44.7200348], [4.3507018, 44.7201359], [4.3506394, 44.7201624], [4.3505637, 44.7201523], [4.3505471, 44.7201097], [4.3506105, 44.7199446], [4.3507489, 44.7197206], [4.3508342, 44.7195634], [4.3508422, 44.7194188], [4.3508945, 44.719223], [4.3508544, 44.7191895], [4.3508079, 44.7191894], [4.350637, 44.7193491], [4.3506135, 44.7193258], [4.3505944, 44.719343], [4.3504867, 44.7194564], [4.350484, 44.7195986], [4.3502451, 44.7198674], [4.3500069, 44.7200707], [4.3496967, 44.7202445], [4.349487, 44.7204725], [4.349424, 44.7205964], [4.3493213, 44.7208001], [4.3491583, 44.7211217], [4.3490871, 44.721281], [4.3490735, 44.7213622], [4.3490977, 44.7214464], [4.3491187, 44.7215189], [4.3491253, 44.7215372], [4.3490344, 44.7216268], [4.3487326, 44.7218522], [4.3487208, 44.7218353], [4.3486707, 44.7218095], [4.3485959, 44.7217566], [4.3485705, 44.7217283], [4.3485133, 44.7216648], [4.3483297, 44.7215049], [4.3482781, 44.7214679], [4.3481933, 44.7213836], [4.3481438, 44.7213406], [4.3481063, 44.7213122], [4.3480237, 44.7212496], [4.3479722, 44.7212107], [4.3475218, 44.720912], [4.347272, 44.7208448], [4.3471404, 44.7207845], [4.3467647, 44.7206689], [4.3466605, 44.7207801], [4.3466377, 44.7217131], [4.3460366, 44.7213886], [4.3459405, 44.7212999], [4.3454985, 44.7210539], [4.3451177, 44.7208197], [4.344361, 44.7202232], [4.3443571, 44.7202202], [4.3434671, 44.7206318], [4.3432126, 44.7208007], [4.3431381, 44.7208827], [4.3430509, 44.7210016], [4.3430025, 44.7211038], [4.3429471, 44.7212121], [4.3427638, 44.7215531], [4.3422504, 44.7218023], [4.3416514, 44.7223177], [4.3414113, 44.7225321], [4.3412989, 44.722677], [4.3412209, 44.7227487], [4.3411191, 44.7228176], [4.3408065, 44.7229798], [4.3406709, 44.7230189], [4.3407531, 44.7231786], [4.3408994, 44.7234163], [4.3410626, 44.7236788], [4.3410904, 44.7242561], [4.3411098, 44.7246246], [4.3411155, 44.7246391], [4.3410102, 44.7245527], [4.340876, 44.7245189], [4.3405702, 44.7245277], [4.3403086, 44.7244837], [4.3398711, 44.7244866], [4.3397956, 44.7245302], [4.3396347, 44.7245387], [4.3395002, 44.7244977], [4.3393194, 44.7244998], [4.3391897, 44.7243648], [4.3391141, 44.7246257], [4.3391149, 44.7246604], [4.3390966, 44.7246693], [4.3390887, 44.7246879], [4.339129, 44.7247353], [4.3391231, 44.7247509], [4.3390602, 
        44.7247612], [4.3390404, 44.724751], [4.3390209, 44.7247528], [4.3389757, 44.7248565], [4.338892, 44.7252133], [4.338773, 44.72535], [4.3387387, 44.7253858], [4.3386511, 44.7254861], [4.3385212, 44.7256347], [4.3380505, 44.7261604], [4.3379866, 44.7262317], [4.3379433, 44.7262802], [4.3378995, 44.7263051], [4.3378764, 44.7263245], [4.337909, 44.7263433], [4.3378805, 44.7263703], [4.3377958, 44.7264511], [4.3377866, 44.7264677], [4.3378282, 44.7264843], [4.3379408, 44.7265295], [4.3380414, 44.7265836], [4.338117, 44.7266417], [4.3381394, 44.7267136], [4.3381241, 44.7267241], [4.3380786, 44.7266775], [4.3380039, 44.726713], [4.3379893, 44.7267014], [4.3379433, 44.7267254], [4.3379654, 44.7267473], [4.3379553, 44.726757], [4.3379777, 44.726784], [4.3378547, 44.7268401], [4.3377582, 44.7268841], [4.3377505, 44.7268876], [4.3376969, 44.7268905], [4.3376269, 44.7269204], [4.3375586, 44.7269494], [4.3373005, 44.7270594], [4.3372403, 44.7270947], [4.3371779, 44.7271205], [4.3371412, 44.7271445], [4.3370237, 44.7272483], [4.3369762, 
        44.7272975], [4.3369074, 44.7274037], [4.3368724, 44.727455], [4.3368561, 44.7274676], [4.336814, 44.7274829], [4.3367223, 44.7274987], [4.336515, 44.7275645], [4.3364136, 44.7276489], [4.3363268, 44.7276964], [4.3362959, 44.7277042], [4.336159, 44.7278207], [4.3360665, 44.727849], [4.3360529, 44.7278589], [4.335727, 44.7280969], [4.3352658, 44.7283697], [4.3350337, 44.7287121], [4.3346195, 44.7289056], [4.3343926, 44.7291617], [4.3340161, 44.7295851], [4.3352772, 44.7305298], [4.3352918, 44.7305399], [4.3353252, 44.7305651], [4.3352016, 44.730726], [4.3347529, 44.7313107], [4.3346876, 44.7313918], [4.3345674, 44.7315563], [4.334557, 44.7315614], [4.3345505, 44.7315657], [4.3344726, 44.7316687], [4.3344518, 44.7316957], [4.3343655, 44.7318077], [4.333852, 44.7324682], [4.3338318, 44.7324957], [4.3326335, 44.7340448], [4.331859, 44.7350457], [4.3312683, 44.7358062], [4.3311208, 44.7359988], [4.330966, 44.7361944], [4.3308646, 44.7363275], [4.3306577, 44.7365944], [4.3303955, 44.736929], [4.3289562, 44.7376237], [4.3273102, 44.7384092], [4.3265481, 44.7387767], [4.3252368, 44.7394027], [4.3239276, 44.7400313], [4.3234268, 44.7402727], [4.318232, 44.7398837], [4.316281, 44.7397317], [4.3162488, 44.7392285], [4.3162769, 44.7389181], [4.3162762, 44.7388611], [4.3162712, 44.7388042], [4.3162662, 44.7387708], [4.3162435, 44.7387225], [4.3161617, 44.7385828], [4.3161149, 44.738486], [4.3160973, 44.7384272], [4.3160839, 44.738368], [4.3160748, 44.7383089], [4.3159189, 44.7377818], [4.3159279, 44.7377632], [4.3159269, 44.7376792], [4.3158903, 44.7375249], [4.3158275, 44.7373061], [4.3157697, 44.7371808], [4.3160216, 44.7370681], [4.3161463, 44.7370026], [4.3162776, 44.7369487], [4.3163454, 44.7368905], [4.3164386, 44.7368516], [4.3165296, 44.7368101], [4.3166289, 44.7367604], [4.3167294, 44.7367218], [4.3169194, 44.7366156], [4.3172106, 44.73642], [4.31732, 44.7363591], [4.3173481, 44.7363669], [4.3175197, 44.7362735], [4.3175793, 44.7362544], [4.3176423, 44.7362506], [4.3178077, 44.7362038], [4.3178495, 44.7361776], [4.3180057, 44.7360461], [4.3181718, 
        44.735938], [4.3183514, 44.7357857], [4.3184149, 44.735754], [4.3190232, 44.7355399], [4.3191546, 44.7354957], [4.3195219, 44.7353198], [4.3196681, 44.7352566], [4.3198165, 44.7351961], [4.3199669, 44.7351383], [4.32002, 44.7351187], [4.3201042, 44.7350942], [4.3207128, 44.734981], [4.3211365, 44.7348295], [4.3213464, 44.7347813], [4.3203394, 44.7324946], [4.3205447, 44.7316494], [4.3205354, 44.7315685], [4.3205576, 44.7315219], [4.3205651, 44.7315063], [4.3205642, 44.7314207], [4.3205004, 44.7312536], [4.3204964, 
        44.7311917], [4.3204876, 44.7310541], [4.320444, 44.7308675], [4.3203307, 44.7305718], [4.3203293, 44.7305624], [4.3203323, 44.7305534], [4.320339, 44.7305455], [4.3203491, 44.7305394], [4.3203613, 44.730536], [4.3203743, 44.7305355], [4.3203867, 44.7305381], 
        [4.3204816, 44.730565], [4.3205447, 44.730534], [4.3205634, 44.7305249], [4.3205404, 44.7304714], [4.3204947, 44.7304115], [4.3204047, 44.7303316], [4.3203734, 44.7303076], [4.3202591, 44.7302625], [4.320201, 44.7302396], [4.3201349, 44.7300621], [4.3199534, 44.7298984], [4.3199316, 44.7298514], [4.3197896, 44.7297463], [4.3197212, 44.729644], [4.3196602, 44.7295099], [4.3196582, 44.7294693], [4.319621, 44.729385], [4.3195582, 44.729122], [4.319542, 44.7289513], [4.3195437, 44.7288938], [4.3196272, 44.7286107], [4.3196782, 44.7285393], [4.319742, 44.7284782], [4.3198243, 44.7283675], [4.3199045, 44.7283039], [4.3200408, 44.7281093], [4.3201192, 44.7279706], [4.3201737, 44.7279133], [4.3201571, 44.7279098], [4.319967, 44.7278905], [4.3199484, 44.7278915], [4.3199977, 44.7273273], [4.3202341, 44.7266792], [4.3204016, 44.7265219], [4.3204226, 44.7264442], [4.3203655, 44.726386], [4.319945, 44.7261331], [4.3195306, 44.7259647], [4.3189093, 44.7256971], [4.3181682, 44.7255754], [4.3178367, 44.7255497], [4.3178354, 44.7255432], [4.3176848, 44.7254797], [4.3176809, 44.7254488], [4.3176883, 44.725322], [4.31768, 44.7252705], [4.3174859, 44.7252854], [4.317168, 44.7251298], [4.3168562, 44.724967], [4.3162707, 44.7246879], [4.3162986, 44.7246404], [4.3162758, 44.7246159], [4.3162556, 44.724597], [4.3160093, 44.7243864], [4.3159993, 44.7243724], [4.3159729, 44.7238981], [4.3160338, 44.7236356], [4.3160957, 44.7233876], [4.3161534, 44.7232396], [4.316184, 44.7231339], [4.3162243, 44.7230841], [4.3163094, 44.7230154], [4.3164086, 44.7229398], [4.3165109, 44.7228664], [4.3165962, 44.7227482], [4.3165899, 44.7227417], [4.3164153, 44.7226219], [4.3160827, 44.7223236], [4.3162506, 44.722164], [4.3159894, 44.7219578], [4.3159368, 44.7219149], [4.3158216, 44.721828], [4.3153634, 44.7214658], [4.315353, 44.7214585], [4.3156676, 44.7212486], [4.3156591, 44.7212376], [4.3145026, 44.720532], [4.314463, 44.72052], [4.3145284, 44.7204433], [4.3146195, 44.7204018], [4.3148145, 44.7203861], [4.3148852, 44.7203581], [4.3151687, 44.7200941], [4.3152197, 44.7198791], [4.3152531, 44.7196201], [4.3152434, 44.719425], [4.3152552, 44.7191661], [4.3152295, 44.7187702], [4.3152693, 44.7184241], [4.3152686, 
        44.7181228], [4.3153553, 44.7178433], [4.3154289, 44.7177584], [4.3156144, 44.7176429], [4.3156872, 44.7175917], [4.3159674, 44.7173973], [4.3162507, 44.7172053], [4.3164523, 44.7170747], [4.3168056, 44.7168783], [4.3169582, 44.7167734], [4.3170817, 44.716657], [4.317197, 44.7164913], [4.3176861, 44.7157275], [4.3178987, 44.7154872], [4.318315, 44.7151096], [4.3185153, 44.7149135], [4.3187846, 44.7147121], [4.3190511, 44.7144762], [4.3191578, 44.7143475], [4.3193752, 44.7139539], [4.3197804, 44.7133634], [4.3201884, 44.7128539], [4.3203485, 44.7126141], [4.3204273, 44.7124275], [4.3204414, 44.7122872], [4.3204391, 44.7122512], [4.3204229, 44.7119851], [4.3203908, 44.7118042], [4.3204359, 44.7117013], [4.3204882, 44.7116373], [4.3205826, 44.7115617], [4.321131, 44.7113536], [4.3214231, 44.7112021], [4.3217002, 44.7110198], [4.3219543, 44.7107818], [4.3221252, 44.7105729], [4.3221819, 44.7103844], [4.3221497, 44.710196], [4.3220589, 44.7099805], [4.3219324, 44.7098265], [4.3218582, 44.7094783], [4.322091, 44.7090769], [4.3222388, 44.7088497], [4.3223659, 44.7086287], [4.3224275, 44.7083789], [4.322407, 44.708248], [4.322286, 44.7080682], [4.3222493, 44.7079551], [4.3223308, 44.7077642], [4.3224564, 44.7076087], [4.3227535, 44.7072605], [4.3230619, 44.7068288], [4.3232306, 44.7064312], [4.3233238, 44.70631], [4.32344, 44.7061908], [4.3242739, 44.7058643], [4.3249193, 44.7056505], [4.3250823, 44.7055498], [4.3251826, 44.705413], [4.3251921, 44.7053357], [4.3251719, 44.7052637], [4.324953, 44.7050444], [4.3247762, 44.704908], [4.3245606, 44.7047042], [4.3245144, 44.7046267], [4.3245572, 44.7045113], [4.3246097, 44.7042306], [4.3246497, 44.7041286], [4.3247199, 44.704079], [4.3246946, 44.7040102], [4.3247139, 44.7039531], [4.3247887, 44.7038794], [4.3248226, 44.7037788], [4.3248635, 44.7037149], [4.3249422, 44.7035972], [4.3250245, 44.7034809], [4.324994, 44.7033664], [4.3250049, 44.7033354], [4.3250136, 44.7033107], [4.3250377, 44.7032421], [4.3251105, 44.7031219], [4.3254088, 44.7027509], [4.3256656, 44.7024074], [4.3261071, 44.7013281], [4.3262395, 44.7009309], [4.3263333, 44.7006056], [4.3264312, 44.700189], [4.3265213, 44.6999676], [4.326564, 44.6998934], [4.3269762, 44.6995718], [4.3272833, 44.6993016], [4.3274373, 44.6990824], [4.3276579, 44.6986996], [4.3277506, 44.6985887], [4.3279261, 44.6984924], [4.3283312, 44.6983993], [4.32867, 44.6983452]]]]}, 'properties': {'id': '07003', 'nom': 'AIZAC', 'created': '2012-11-29', 'updated': '2014-02-14'}}]}
        self.assertEqual(test6, True)
    

#test fonction telechargement
#t5 = Telechargement(id_zone1="07003",zonage1="communes",zonage2="parcelles")
#test5 = t5.download()  

#lecture de json vers dictionnaire
#t5= Telechargement(id_zone1="07003",zonage1="communes",zonage2="communes")
#t5.download()
#dico = t5.read_json()
#print(dico) 

if __name__ == '__main__':
    unittest.main()