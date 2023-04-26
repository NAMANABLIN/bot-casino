from dotenv import load_dotenv
from os import getenv, getcwd
from json import load, dump

load_dotenv()

VK_TOKEN = getenv("VK_MAIN")

admin_IDs = [221158750, 321346270]

sex2bool = {'Мужской': True,
            'Женский': False}

even_bets = ['чет', 'чёт', 'чётное', 'четное', 'чётный', 'четный', 'even']
odd_bets = ['нечет', 'нечёт', 'нечётное', 'нечетное', 'нечётный', 'нечетный', 'odd']
zero_bets = ['зеро', 'ноль', 'zero']
all_bets = even_bets + odd_bets + zero_bets

path = getcwd()
all_promo_codes = load(open(path + '/' + 'promocodes.json', 'rb'))
images = {
    'win': {0: 'photo221158750_457273376_e2ac38381a9fec1f0f', 1: 'photo221158750_457273377_e2253d296d9097713d',
            2: 'photo221158750_457273378_baa934af3234d2343d', 3: 'photo221158750_457273379_34e3f0472c152ab044',
            4: 'photo221158750_457273380_3c8924098f7d1338b3', 5: 'photo221158750_457273381_1765b6a6bffb433639',
            6: 'photo221158750_457273382_98ff6a501fc7f39e5e', 7: 'photo221158750_457273383_9eb43ab62242ee7ca1',
            8: 'photo221158750_457273384_9fb5522056604c81a6', 9: 'photo221158750_457273385_bd45b75fdfaa5f76b1',
            10: 'photo221158750_457273386_5a59bee48bf3a271ac', 11: 'photo221158750_457273387_c746a5c78ff8d11b02',
            12: 'photo221158750_457273388_63c498bb666d499dfc', 13: 'photo221158750_457273389_feaf5712019b53ab46',
            14: 'photo221158750_457273390_fd9bd9ebed10d8a69a', 15: 'photo221158750_457273391_f391af5c6a68aa14fd',
            16: 'photo221158750_457273392_cac733381585b8e80c', 17: 'photo221158750_457273393_29a8be12e1d69e1bcf',
            18: 'photo221158750_457273394_8696c7257bbdb4a7ff', 19: 'photo221158750_457273395_7ffc5dbd1391406d85',
            20: 'photo221158750_457273396_53529f52bc905cf0e7', 21: 'photo221158750_457273397_c2c9fd5338715404ac',
            22: 'photo221158750_457273398_3900813da3c74894be', 23: 'photo221158750_457273399_a59858cfb47afb5b3d',
            24: 'photo221158750_457273400_7384a2f1020a6d2001', 25: 'photo221158750_457273401_ee77633a7bd1e49b65',
            26: 'photo221158750_457273402_855c55ecb2a0e3e2ff', 27: 'photo221158750_457273403_6e136c45d34c5f9550',
            28: 'photo221158750_457273404_d6f63ab63c111015e6', 29: 'photo221158750_457273405_73bc088fd9294568f8',
            30: 'photo221158750_457273406_8bf81dd08a63be2241', 31: 'photo221158750_457273407_cdee1be992713eae30',
            32: 'photo221158750_457273408_97305d911cb40814ff', 33: 'photo221158750_457273409_988b01199222294cd1',
            34: 'photo221158750_457273410_7d183a1669b2333996', 35: 'photo221158750_457273411_517e221743d73a27df',
            36: 'photo221158750_457273412_f92fb419f7a2087ec7'},
    'lose': {0: 'photo221158750_457273413_fc63dc214be622a3c2', 1: 'photo221158750_457273414_c59013b2205952e28b',
             2: 'photo221158750_457273415_65a15a3ed248a5fdf4', 3: 'photo221158750_457273416_98ae1d387c4648d361',
             4: 'photo221158750_457273417_2b1732d5e298f67102', 5: 'photo221158750_457273418_fe79582f7dfb4ba54f',
             6: 'photo221158750_457273419_2ed424ac7d1f8bc8e9', 7: 'photo221158750_457273420_5d86c63709be62747e',
             8: 'photo221158750_457273421_087a65757ec0c3a9b8', 9: 'photo221158750_457273422_f34e87e056b6306ddf',
             10: 'photo221158750_457273423_7dae7bbff18099ed3a', 11: 'photo221158750_457273424_90434290398a6c9855',
             12: 'photo221158750_457273425_7846494a95e4fee5fe', 13: 'photo221158750_457273426_c6eb97277713f350b6',
             14: 'photo221158750_457273427_ddc870cc5031fbdc0e', 15: 'photo221158750_457273428_27fa4be5ebd854c8c1',
             16: 'photo221158750_457273429_9a2090942cf4b93481', 17: 'photo221158750_457273430_103d5dfc98648a0098',
             18: 'photo221158750_457273431_fe1222d304e3a89ff7', 19: 'photo221158750_457273432_bcd79fcfca5b8b93e5',
             20: 'photo221158750_457273433_1da5a7328fb5a91b2f', 21: 'photo221158750_457273434_5a79dbbec8160d3862',
             22: 'photo221158750_457273435_3cee3afa53ae0832d1', 23: 'photo221158750_457273436_01c00476bbd63ffd85',
             24: 'photo221158750_457273437_0c8a6e208fd5b4517d', 25: 'photo221158750_457273438_4cbe8dd9906f89e134',
             26: 'photo221158750_457273439_5c132bb7d79df4bce3', 27: 'photo221158750_457273440_1d3afeceb195598a19',
             28: 'photo221158750_457273441_8b6cd17957665693d6', 29: 'photo221158750_457273442_3956fafce3256f213d',
             30: 'photo221158750_457273443_2397b83b78997aff3d', 31: 'photo221158750_457273444_4e7561cfcb43bfbbf1',
             32: 'photo221158750_457273445_966777a9a7b121be7c', 33: 'photo221158750_457273446_12d40195db9ac68a35',
             34: 'photo221158750_457273447_580eb15a5562be9e47', 35: 'photo221158750_457273448_5c9e20218237533dc2',
             36: 'photo221158750_457273449_561cb66a6d5382b43d'}}
