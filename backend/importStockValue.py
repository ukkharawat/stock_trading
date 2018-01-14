import csv , sys , os
import numpy as np
import math

project_dir = '/backend/'

sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()

from stockApp.models import Stock , StockValue
syms = [ "CHOTI", "EE", "GFPT", "LEE", "STA", "TLUXE", "TRUBB", "TWPC", "UPOIC", "UVAN", "VPO", "APURE", "ASIAN", "BR", "BRR", "CBG", "CFRESH", "CM", "CPF", "CPI", "F&D", "HTC", "ICHI", "KBS", "KSL", "KTIS", "LST", "M", "MALEE", "MINT", "OISHI", "PB", "PM", "PRG", "SAPPE", "SAUCE", "SFP", "SNP", "SORKON", "SSC", "SSF", "SST", "TC", "TFG", "TFMAMA", "TIPCO", "TKN", "TU", "TVO", "AFC", "BTNC", "CPH", "CPL", "DIGI", "ICC", "LTX", "NC", "PAF", "PG", "PRANDA", "SABINA", "SAWANG", "SUC", "TNL", "TPCORP", "TR", "TTI", "TTL", "TTTM", "UPF", "UT", "WACOAL", "ACC", "AJA", "DTCI", "FANCY", "KYE", "L&E", "MODERN", "OGC", "ROCK", "SIAM", "TSR", "DDD", "JCT", "OCC", "S & J", "STHAI", "TNR", "TOG", "BAY", "BBL", "CIMBT", "KBANK", "KKP", "KTB", "LHBANK", "SCB", "TCAP", "TISCO", "TMB", "AEC", "AEONTS", "AMANAH", "ASAP", "ASK", "ASP", "BFIT", "CGH", "CNS", "ECL", "FNS", "FSS", "GBX", "GL", "IFS", "JMT", "KCAR", "KGI", "KTC", "MBKET", "MFC", "ML", "MTLS", "PE", "PL", "S11", "SAWAD", "THANI", "TK", "TNITY", "UOBKH", "ZMICO", "AYUD", "BKI", "BLA", "BUI", "CHARAN", "INSURE", "MTI", "NKI", "NSI", "SMK", "THRE", "THREL", "TIC", "TIP", "TSI", "TVI", "AH", "APCS", "BAT-3K", "CWT", "EASON", "GYT", "HFT", "IHL", "INGRS", "IRC", "PCSGH", "SAT", "SPG", "STANLY", "TKT", "TNPC", "TRU", "TSC", "YNP", "ALLA", "ASEFA", "CPT", "CRANE", "CTW", "FMT", "HTECH", "KKC", "PK", "SNC", "TCJ", "VARO", "AJ", "ALUCON", "CSC", "NEP", "NPP", "PTL", "SITHAI", "SLP", "SMPC", "SPACK", "TCOAT", "TFI", "THIP", "TMD", "TOPP", "TPBI", "TPP", "UTP", "GC", "GGC", "GIFT", "IVL", "PATO", "PMTA", "PTTGC", "SUTHA", "TCB", "TCCC", "TPA", "UP", "VNT", "WG", "YCI", "AMC", "BSBM", "CEN", "CITY", "CSP", "GJS", "GSTEL", "INOX", "LHK", "MAX", "MCS", "MILL", "PAP", "PERM", "RICH", "SAM", "SMIT", "SSI", "SSSC", "TGPRO", "THE", "TIW", "TMT", "TSTH", "TUCC", "TWP", "TYCN", "CCP", "DCC", "DCON", "DRT", "EPG", "GEL", "PPP", "Q-CON", "RCI", "SCC", "SCCC", "SCP", "SKN", "TASCO", "TCMC", "TGCI", "TOA", "TPIPL", "UMI", "VNG", "WIIK", "BJCHI", "CK", "CNT", "EMC", "ITD", "NWR", "PAE", "PLE", "PREB", "PYLON", "SEAFCO", "SQ", "SRICHA", "STEC", "STPI", "SYNTEC", "TPOLY", "TRC", "TTCL", "UNIQ", "A", "AMATA", "AMATAV", "ANAN", "AP", "APEX", "AQ", "BLAND", "BROCK", "CGD", "CI", "CPN", "ESTAR", "EVER", "GLAND", "GOLD", "GREEN", "J", "KC", "KWG", "LALIN", "LH", "LPN", "MBK", "MJD", "MK", "NCH", "NNCL", "NOBLE", "NUSA", "ORI", "PACE", "PF", "PLAT", "POLAR", "PRECHA", "PRIN", "PRINC", "PSH", "QH", "RICHY", "RML", "ROJNA", "S", "SAMCO", "SC", "SENA", "SF", "SIRI", "SPALI", "TFD", "TICON", "U", "UV", "WHA", "WIN", "AMATAR", "BKKCP", "CPNCG", "CPNREIT", "CPTGF", "CRYSTAL", "CTARAF", "DREIT", "ERWPF", "FUTUREPF", "GAHREIT", "GLANDRT", "GOLDPF", "GVREIT", "HPF", "HREIT", "IMPACT", "JCP", "KPNPF", "LHHOTEL", "LHPF", "LHSC", "LUXF", "M-II", "MIPF", "MIT", "MJLF", "MNIT", "MNIT2", "MNRF", "MONTRI", "M-PAT", "M-STOR", "POPF", "PPF", "QHHR", "QHOP", "QHPF", "SBPF", "SHREIT", "SIRIP", "SPF", "SRIPANWA", "SSPF", "SSTPF", "SSTRT", "TIF1", "TLGF", "TLHPF", "TNPF", "TPRIME", "TREIT", "TTLPF", "TU-PF", "URBNPF", "WHABT", "WHART", "ABPIF", "AI", "AKR", "BAFS", "BANPU", "BCP", "BCPG", "BGRIM", "BPP", "BRRGIF", "CKP", "DEMCO", "EA", "EARTH", "EASTW", "EGATIF", "EGCO", "ESSO", "GLOW", "GPSC", "GULF", "GUNKUL", "IEC", "IFEC", "IRPC", "LANNA", "MDX", "PTG", "PTT", "PTTEP", "RATCH", "RPC", "SCG", "SCI", "SCN", "SGP", "SKE", "SOLAR", "SPCG", "SPRC", "SUPER", "SUSCO", "TAE", "TCC", "TOP", "TPIPP", "TTW", "WHAUP", "PDI", "THL", "BEAUTY", "BIG", "BJC", "COL", "COM7", "CPALL", "CSS", "FN", "FTE", "GLOBAL", "HMPRO", "IT", "KAMART", "LOXLEY", "MAKRO", "MC", "MEGA", "MIDA", "ROBINS", "RSP", "SINGER", "SPC", "SPI", "AHC", "BCH", "BDMS", "BH", "CHG", "CMR", "EKH", "KDH", "LPH", "M-CHAI", "NEW", "NTV", "RAM", "RJH", "RPH", "SKR", "SVH", "THG", "VIBHA", "VIH", "WPH", "AMARIN", "AQUA", "AS", "BEC", "EPCO", "FE", "GPI", "GRAMMY", "MACO", "MAJOR", "MATCH", "MATI", "MCOT", "MONO", "MPIC", "NMG", "PLANB", "POST", "PRAKIT", "RS", "SE-ED", "SMM", "SPORT", "TBSP", "TH", "TKS", "TRITN", "VGI", "WAVE", "WORK", "BWG", "GENCO", "PRO", "ASIA", "CENTEL", "CSR", "DTC", "ERW", "GRAND", "LRH", "MANRIN", "OHTL", "ROH", "SHANG", "AAV", "AOT", "ASIMAR", "BA", "BEM", "BTC", "BTS", "BTSGIF", "III", "JUTHA", "JWD", "KWC", "NOK", "NYT", "PRM", "PSL", "RCL", "THAI", "TSTE", "TTA", "WICE", "CCET", "DELTA", "EIC", "HANA", "KCE", "METCO", "SMT", "SPPT", "SVI", "TEAM", "ADVANC", "AIT", "ALT", "BLISS", "CSL", "DIF", "DTAC", "FER", "FORTH", "HUMAN", "ILINK", "INET", "INTUCH", "JAS", "JASIF", "JMART", "JTS", "MFEC", "MSC", "PT", "SAMART", "SAMTEL", "SDC", "SIS", "SVOA", "SYMC", "SYNEX", "THCOM", "TRUE", "TWZ	", ]

for sym in syms:
	try:
		data = csv.reader(open("stockData/" + sym + '.BK.csv'), delimiter=",")
		insertList = []
		for row in data:
			if row[0] != 'Date':
				stockvalue = StockValue()
				stockvalue.name = Stock.objects.get(name=sym)
				stockvalue.date = row[0]
				if row[1] is "":
					stockvalue.openPrice = np.nan
					stockvalue.closePrice = np.nan
					stockvalue.high = np.nan
					stockvalue.low = np.nan
					stockvalue.adjClose = np.nan
					stockvalue.volume = np.nan
				else:
					stockvalue.openPrice = row[1]
					stockvalue.closePrice = row[2]
					stockvalue.high = row[3]
					stockvalue.low = row[4]
					stockvalue.adjClose = row[5]
					stockvalue.volume = row[6]
				insertList.append(stockvalue)
		StockValue.objects.bulk_create(insertList)
		print sym + " DONE"
	except Exception, e:
		print sym + " ERROR " + str(e)