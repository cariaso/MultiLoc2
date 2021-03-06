import re, os, sys, util

def searchNLS(sequence):
	predictNLS=0
	nlsdb=[]
	nlsdb.append("APKRKSGVSKC")
	nlsdb.append("APTKRKGS")
	nlsdb.append("CKRKTTNADRRKA")
	nlsdb.append("CYGSKNTGAKKRKIDDA")
	nlsdb.append("DK[QL]KK[QL]")
	nlsdb.append("DR[MN]KKKKE")
	nlsdb.append("D[KR].{0,1}[QL][RK]{2,3}R")
	nlsdb.append("EEDGPQKKKRRL")
	nlsdb.append("EYLSRKGKLEL")
	nlsdb.append("GGG.{3}KNRR.{6}RGGRN")
	nlsdb.append("GKKKYKLKH")
	nlsdb.append("GKKRSKA")
	nlsdb.append("GRKRKKRT")
	nlsdb.append("GR[RK]{2,4}..[RK][QL]")
	nlsdb.append("G{2,4}[RK].{1,3}G{3}")
	nlsdb.append("HKKKKIRTSPTFTTPKTLRLRRQPKYPRKSAPRRNKLDHY")
	nlsdb.append("HRIEEKRKRTYETFKSI")
	nlsdb.append("HRKYEAPRH.{6}PRKR")
	nlsdb.append("IKYFKKFPKD")
	nlsdb.append("KAKRQR")
	nlsdb.append("KDCVINKHHRNRCQYCRLQR")
	nlsdb.append("KHLKGR")
	nlsdb.append("KHRKHPG")
	nlsdb.append("KKEKKKSKK")
	nlsdb.append("KKKKKEEEGEGKKK")
	nlsdb.append("KKKKK.{3,6}KK")
	nlsdb.append("KKKKRKREK")
	nlsdb.append("KKKKR[KR]")
	nlsdb.append("KKKRERLD")
	nlsdb.append("KKKRRSREK")
	nlsdb.append("KKKR[KR][VPL]")
	nlsdb.append("KKKYKLK")
	nlsdb.append("KKP.{6,9}K.{1,3}RK")
	nlsdb.append("KKQTTLAFKPIKKGKKR")
	nlsdb.append("KKRKRT")
	nlsdb.append("KKRKR[KR]")
	nlsdb.append("KKRKR[ST]")
	nlsdb.append("KKRRK")
	nlsdb.append("KKRR[DE]K")
	nlsdb.append("KKRR.K")
	nlsdb.append("KKSKKGRQEALERLKKA")
	nlsdb.append("KK[MNQSTC]R[MNQSTC]K[MNQSTC]")
	nlsdb.append("KK.R.{3,5}R[PVL]K")
	nlsdb.append("KK.{1,7}K[PL][PLIV]KK")
	nlsdb.append("KK.{15}KKRK")
	nlsdb.append("KRAAEDDEDDDVDTKKQK")
	nlsdb.append("KRGRGRPRK")
	nlsdb.append("KRKKEMANKSAPEAKKKK")
	nlsdb.append("KRKRRP")
	nlsdb.append("KRK.{0,8}KR[PL]K")
	nlsdb.append("KRK.{10,14}[KR]{3,}?.[KR]K")
	nlsdb.append("KRK.{11}KKKSKK")
	nlsdb.append("KRK.{2,4}DRRK")
	nlsdb.append("KRK.{22}KELQKQITK")
	nlsdb.append("KRK.{5,10}KK[PL]K")
	nlsdb.append("KRMRNRIAASKCRKRKL")
	nlsdb.append("KRPAATKKAGQAKKKK")
	nlsdb.append("KRPACTLKPECVQQLLVCSQEAKK")
	nlsdb.append("KRPAEDMEEEQAFKRSR")
	nlsdb.append("KRPMNAFIVWSRDQRRK")
	nlsdb.append("KRPMNAFMVWAQAARRK")
	nlsdb.append("KRPRP")
	nlsdb.append("KRQR.{20}KKSKK")
	nlsdb.append("KRSAEGGNPPKPLKKLR")
	nlsdb.append("KR[GPL]R[GPL]R[GLP]RK")
	nlsdb.append("KR[MNSQ]R[MNSQ]R")
	nlsdb.append("KR[PLV][GA]KRK[PL]")
	nlsdb.append("KR[RK][RK].{2,4}[RK].{0,2}R.{3,5}[RK].{0,2}[RK].{0,2}[RK][RK]K")
	nlsdb.append("KR[ST]R..R{2,4}[QL]K")
	nlsdb.append("KR.R.R.{2,6}RKRK")
	nlsdb.append("KR.R..RRLK")
	nlsdb.append("KR.[DE][KR][KR].K")
	nlsdb.append("KR..KK.K[DE]")
	nlsdb.append("KR.{1,3}H.{3,5}R[LQ]RR")
	nlsdb.append("KR.{10}KKKL")
	nlsdb.append("KR.{7,9}PQPKKKP")
	nlsdb.append("KR.{9}KTKK")
	nlsdb.append("KR{2,4}.{3,6}[RK]{2,4}.{0,2}KR")
	nlsdb.append("KR{3,}?[LVI]")
	nlsdb.append("KSKKKAQ")
	nlsdb.append("KTRKHRG")
	nlsdb.append("KVNSRKRRKEVPGPNGATEED")
	nlsdb.append("KVTKRKHDNEGSGSKRPK")
	nlsdb.append("K[GA]K[AG]KK[AG]")
	nlsdb.append("K[IVQM]RR[VI][STK]L")
	nlsdb.append("K[KR][KR]RR[KR]")
	nlsdb.append("K[KR][QMN][RK]R[QMN]R")
	nlsdb.append("K[MNQ]RR[PLVI]K[PL]")
	nlsdb.append("K[PLMN]RRK[MNQ]")
	nlsdb.append("K[PL]K{2,3}.{1,3}[RK]{2,4}.{6,9}K[KR]")
	nlsdb.append("K[PL]K{3,}?.KK")
	nlsdb.append("K[RK]{2,4}[ST]H")
	nlsdb.append("K[RK]{2,}?[QL].{3,8}R{3}")
	nlsdb.append("K[RK]{3,5}.{11,18}[RK]K.{2,3}K")
	nlsdb.append("K.KRQR")
	nlsdb.append("K.K.K.....RKK")
	nlsdb.append("K.[PLV][RK][RK]RK")
	nlsdb.append("K..K.K.K.....RKK")
	nlsdb.append("K{1,}?R{2,}?[QM]R{2,}")
	nlsdb.append("K{3,4}R{2,3}")
	nlsdb.append("LEKKVKKKFDWCA")
	nlsdb.append("LKDVRKRKLGPGH")
	nlsdb.append("LKKIKQ")
	nlsdb.append("LKRKLQR")
	nlsdb.append("LKRPRSPSS")
	nlsdb.append("MAPSAKATAAKKAVVKGTNGKKALKVRTSATFRLPKTLKLAR")
	nlsdb.append("MNKIPIKDLLNPG")
	nlsdb.append("MPKTRRRPRRSQRKRPPT")
	nlsdb.append("MPTEERVRKRKESNRESARRSRYRKAAHLK")
	nlsdb.append("NQSSNFGPMKGGNFGGRSSGPYGGGGQYFAKPRNQGGY")
	nlsdb.append("N[QR]RQ[RK][EG]KR[IVLS]")
	nlsdb.append("PAAKRVKLD")
	nlsdb.append("PAKRARRGYK")
	nlsdb.append("PKKARED")
	nlsdb.append("PKKKRKV")
	nlsdb.append("PKKK.RK")
	nlsdb.append("PKKNRLRRP")
	nlsdb.append("PKRPRDRHDGELGGRKRARG")
	nlsdb.append("PKRP.{5,8}L.{2,4}R.K.K")
	nlsdb.append("PK[KR][KRP][RAK][KT][VSE]")
	nlsdb.append("PLLKKIKQ")
	nlsdb.append("PNKKKRK")
	nlsdb.append("PPQKKIKS")
	nlsdb.append("PPRIYPQLPSAPT")
	nlsdb.append("PPRKKRTVV")
	nlsdb.append("PPVKRERTS")
	nlsdb.append("PQPKKKP")
	nlsdb.append("PQSRKKLR")
	nlsdb.append("PRGRRQPIPKARQP")
	nlsdb.append("PRPRKIPR")
	nlsdb.append("PRRGPR")
	nlsdb.append("PRRRK")
	nlsdb.append("PYLNKRKGKP")
	nlsdb.append("P.[PQLVMN][KR]{2,3}.KQ")
	nlsdb.append("QNRR.K.[RK][RK][DQE]")
	nlsdb.append("QRKRQK")
	nlsdb.append("Q[RK][HRK][RK].RR")
	nlsdb.append("RAIKRRPGLDFDDDGEGNSKFLR")
	nlsdb.append("REKKEKEQKEKCA")
	nlsdb.append("RER[MNQ]K.{4,8}R[MNQ]RR")
	nlsdb.append("RGRRRRQR")
	nlsdb.append("RH[RK]H.{2,4}[RK]{2,4}[PL]R")
	nlsdb.append("RIRKKLR")
	nlsdb.append("RKCLQAGMNLEARKTKK")
	nlsdb.append("RKEWLTNFMEDRRQRKL")
	nlsdb.append("RKKRKR")
	nlsdb.append("RKKRK.{9}KAKKSK")
	nlsdb.append("RKKRRQRRR")
	nlsdb.append("RKKRR.R")
	nlsdb.append("RKRAFHGDDPFGEGPPDKK")
	nlsdb.append("RKRIREDRKATTAQKVQQMKQRLNENERKRKR")
	nlsdb.append("RKRKK")
	nlsdb.append("RKRKKMPASQRSKRRKT")
	nlsdb.append("RKRKR[KR]")
	nlsdb.append("RKRRR")
	nlsdb.append("RKR[PLQMN]R[PLQMN]R")
	nlsdb.append("RKR.{12,16}RRKK")
	nlsdb.append("RKR{3,5}[ST]")
	nlsdb.append("RK[IVE]W[ML][TQR]N[HF]")
	nlsdb.append("RK[PL][PLV]KK[RKH]")
	nlsdb.append("RK[RK][QML][RK].R")
	nlsdb.append("RK]{2,4}[PL][RK].{7,11}[RK][QL]KH")
	nlsdb.append("RK.{7,12}RK[STMNQ]KK")
	nlsdb.append("RLKKLKCSK.{19}KTKR")
	nlsdb.append("RPRRK")
	nlsdb.append("RQARRNRRRRWR")
	nlsdb.append("RRERNKMAAAKCRNRRR")
	nlsdb.append("RRER[MNQ]K.{4,8}R[MNQ]RRR")
	nlsdb.append("RRER.{4}RPRKIPR")
	nlsdb.append("RRKGKEK")
	nlsdb.append("RRK.{3,5}R[DE]R{3,}?[PLV]")
	nlsdb.append("RRK.{5,7}RRR")
	nlsdb.append("RRMKWKK")
	nlsdb.append("RRPS.{22}RRKRQ")
	nlsdb.append("RRRKKR")
	nlsdb.append("RRRK[STC]K")
	nlsdb.append("RRRRRR")
	nlsdb.append("RRRRRR.{0,2}R")
	nlsdb.append("RRRRR.RR")
	nlsdb.append("RRR[LP]..R[PLQ]")
	nlsdb.append("RRR[PL]RK")
	nlsdb.append("RRR.{11}KRRK")
	nlsdb.append("RRR{3,5}T")
	nlsdb.append("RRSMKRK")
	nlsdb.append("RR[PLIV]RK.K")
	nlsdb.append("RR[PLQMN].RRRR")
	nlsdb.append("RR[TS].[QK][KR][KNS]")
	nlsdb.append("RR[TS].[QK][KR][KN]")
	nlsdb.append("RR.KR.K[PLV]")
	nlsdb.append("RR.RRRRR")
	nlsdb.append("RR.R[PVL]RK")
	nlsdb.append("RR.R.K.KQ")
	nlsdb.append("RR.R.RKQ")
	nlsdb.append("RR..KRK")
	nlsdb.append("RR.{0,1}RRRRR")
	nlsdb.append("RVHPYQR")
	nlsdb.append("R[GA][IVLP]KRR")
	nlsdb.append("R[GA].{0,2}[GA]R[GA].[GA]R[GA]")
	nlsdb.append("R[GVLIP]RRRR.R")
	nlsdb.append("R[IVLP][IVLP]KRR")
	nlsdb.append("R[KR]RRRR.R")
	nlsdb.append("R[KR][RK].{0,2}[RK].{0,2}[RK].{3,5}[RK].{0,2}[RK][RK][RK][RK][PMQL]")
	nlsdb.append("R[KR]{3,4}K[DE]")
	nlsdb.append("R[MNQ]RRRR.R")
	nlsdb.append("R[MNQ].{4,8}R[MNQ]RR")
	nlsdb.append("R[PL].G.[KR][KR].K")
	nlsdb.append("R[PL]..[KR]{2,}?..[KR]V")
	nlsdb.append("R[QMPL]RR[DE]R")
	nlsdb.append("R[RK]K[RK]KR")
	nlsdb.append("R[RK].[KR].[RK]{2,}?[DE]")
	nlsdb.append("R[RK].{4,6}[RK][RK].[RK].{1,3}[RK][RK][PLQ]")
	nlsdb.append("R[RK]{2,4}[PL][RK][MNQ]R")
	nlsdb.append("R[RK]{2,4}.{15,19}[RK]{2,4}[QLM]K")
	nlsdb.append("R[RK]{3,}?[DE]K")
	nlsdb.append("R[STCMNQ]R[STCMNQ]KR")
	nlsdb.append("R.KKKK[DE]")
	nlsdb.append("R.RR.{4,6}RKK")
	nlsdb.append("R.RSRS.{0,1}R.R")
	nlsdb.append("R.R.R.R.R.R")
	nlsdb.append("R.R.R.R.R.R.K")
	nlsdb.append("R.R{2,}?[QL].[ST]R")
	nlsdb.append("R.[KR][KR]K[PLQM]R")
	nlsdb.append("R.[KR][KR][KR]..RKKR")
	nlsdb.append("R.{2,3}H.{3,5}RRRR")
	nlsdb.append("R.{2,3}RRRRRR")
	nlsdb.append("R{2,3}K{3,4}[PLRKE]")
	nlsdb.append("R{2,3}.K{2,3}R[ST]")
	nlsdb.append("R{2,}?PR{3,}?")
	nlsdb.append("R{2,}?[QMN]R{3,}?")
	nlsdb.append("SANKVTKNKSNSSPYLNKRGKPGPDS")
	nlsdb.append("SDKKVRSRLIECA")
	nlsdb.append("SKRVAKRKL")
	nlsdb.append("S.GTKRSY..M")
	nlsdb.append("TEKK[QG]KSILYDCA")
	nlsdb.append("TKRS...M")
	nlsdb.append("T[PLV]KRC")
	nlsdb.append("VNEAFETLKRC")
	nlsdb.append("VSRKRPR")
	nlsdb.append("WKQ[KR]RKF")
	nlsdb.append("YKRPCKRSFIRFI")
	nlsdb.append("YLTQETNKVETYKEQPLKTPGKKKKGKP")
	nlsdb.append("YNNQSSNFGPMKGGN")
	nlsdb.append("[DE]KK[PL][GL]K[GL]")
	nlsdb.append("[DE]KR[MQN]R[MQN]R")
	nlsdb.append("[DE]K[NIF]RR[DEK][STMNQ]")
	nlsdb.append("[DE]K.RRK[MNQ]")
	nlsdb.append("[DE]RKRR[DEPLQ]")
	nlsdb.append("[DE]R.KKKK")
	nlsdb.append("[DE]R{2,4}.RK[PL]")
	nlsdb.append("[DE][KR]RR[KR][FYW]")
	nlsdb.append("[DE][RK]{2,4}[GA]R[PL][GA]")
	nlsdb.append("[DE][RK]{3,}?.[KR]{2,}?[PL]")
	nlsdb.append("[DE][ST][PL]KR[STC]")
	nlsdb.append("[ED]R{4,}?[ED]")
	nlsdb.append("[GAPLV]RKRKKR")
	nlsdb.append("[GA]K.KKK[MNQ]")
	nlsdb.append("[GA]R.[RK].[RK][RK].[QM]")
	nlsdb.append("[GA][KR]KR.[KR][GA]")
	nlsdb.append("[KAR]TPIQKHWRPTVLTEGPPVKIRIETGEWE[KA]")
	nlsdb.append("[KR]G{2,}?..G{3,}?[RK]")
	nlsdb.append("[KR]KRKK")
	nlsdb.append("[KR]XXKNKX{6,8}K[KR]")
	nlsdb.append("[KR][DE][KR][DE]..[KR]{4,}?")
	nlsdb.append("[KR][KR][KR][KR][KR][KR][KR]")
	nlsdb.append("[KR][KR][QMN]R[RK][QMN]R")
	nlsdb.append("[KR][KR].[KR][KR][KR].[KR][KR]")
	nlsdb.append("[KR]{2,3}..KR[KR][QLM]")
	nlsdb.append("[KR]{2,}?[PL].{1,4}[KR]{2,}?.{1,5}K{3,}?")
	nlsdb.append("[KR]{2}.{0,1}[KR]{2,4}.{25,34}K{2,4}.{1,2}K")
	nlsdb.append("[KR]{4}.{20,24}K{1,4}.K")
	nlsdb.append("[LF][STK][VIQM][KR]R[QMVI][STK]L")
	nlsdb.append("[MI]VWSRD[HEQ]RRK")
	nlsdb.append("[PLQMKR]R[KR][QM][KR]R.K")
	nlsdb.append("[PLQMNKR]K[KR][KR]R.K[PLQMNKR]")
	nlsdb.append("[PLQ]K[RK].{1,2}[RK].{3,6}[RK][RK].{1,2}[RK].{1,2}[RK][RK]")
	nlsdb.append("[PLQ][KR].{3,4}KKRK")
	nlsdb.append("[PLV]K[RK].[QMN][RK]R")
	nlsdb.append("[PLV]K[RK].[RK][RK][RK][PL]")
	nlsdb.append("[PLV]RK[ST]R[DE]K")
	nlsdb.append("[PL]K..KRR")
	nlsdb.append("[PL]RKRK[PL]")
	nlsdb.append("[PL]R[DE]K[DE]R")
	nlsdb.append("[PL][KR]{5,7}[PL]")
	nlsdb.append("[PL][PL].[KR]R[DE][KR][QST]")
	nlsdb.append("[PL][RK][RK][DEP]R[RK][FYW]")
	nlsdb.append("[PL][RK][RK][KR][GAPL][RK][STQM]")
	nlsdb.append("[PL][RK]{2,3}K[PLI][RK].[PLI].K")
	nlsdb.append("[PL]..KR[IV]K[PL][DE]")
	nlsdb.append("[PVLI][RK][RK][RK][RK][RK][QMN]K")
	nlsdb.append("[QL]K{2,4}.{8,12}[RK][QL][RK][QL]KR")
	nlsdb.append("[QL].KR.K.KK")
	nlsdb.append("[QMN]R[RK].K.[RK][RK]")
	nlsdb.append("[RK]H[RK]...[RK]{2,4}.R")
	nlsdb.append("[RK]K{2,4}.[RK][QL][RK][PL]")
	nlsdb.append("[RK]R[MS]K.K[KR]")
	nlsdb.append("[RK][PLIV][KR][RK]{2,4}[PLVI]R")
	nlsdb.append("[RK].[RK].[KR].{4,6}RKK")
	nlsdb.append("[RK]{2,4}.{1,2}[RK].{0,2}[RK].{3,5}[RK].{0,2}[RK][RK]{2,4}[PL]")
	nlsdb.append("[RK]{2,4}.{2,4}[QLM][RK].{2,3}[RK]KR")
	nlsdb.append("[RK]{3,}?.[RK].[RK].{4,9}[RK]{3,}?")
	nlsdb.append("[RK]{3,}?.{8,16}[RK]{4,}?")
	nlsdb.append("[RK]{4,}?[QMNPL][RK].{3,4}[RK]{2}")
	nlsdb.append("[STQM]RKRK[STQM]")
	nlsdb.append("[STQM]RKRR[STQM]")
	nlsdb.append("[STQM]RRRK[STQM]")
	nlsdb.append("[ST]G.{1,3}G{3,}?.{1,2}G{3,}?[ST]")
	nlsdb.append("[TS][RK]KK[VLI]R[PL]")
	nlsdb.append("[YFW]RRRR[PL]")
	for nls in nlsdb:
		if len(re.findall(nls,sequence))>0:
			predictNLS=1
			break
	return predictNLS

def search_nuc_domain(sequence):
	dna_associated_domain=0
	dna_associated_domain_desc=""
	domaindb=[]
	domaindb.append("[LIVMFYG][ASLVR]..[LIVMSTACN].[LIVM]....[LIV][RKNQESTAIY][LIVFSTNKH]W[FYVC].[NDQTAH].....[RKNAIMW]")
	domaindb.append("C.{2,4}C...[LIVMFYWC]........H.{3,5}H")
	domaindb.append("[KR].{1,3}[RKSAQ]N..[SAQ][SAQ].[RKTAENQ].R.[RK]")
	domaindb.append("[DENSTAP][KR][LIVMAGSNT][^FYWCPHKR][LIVMT][LIVM]..[STAV][LIVMSTACKR].[VMFYH][LIVMTA]^P^P[LIVMRKHQ]")
	domaindb.append("C.H.[LIVMFY]C..C[LIVMYA]")
	domaindb.append("W.C.{2,4}C...N......C..C")
	domaindb.append("[CH].{2,4}C.{7,17}C.{0,2}C....[YFT]C...[CH].{6,9}H.{3,4}C")
	domaindb.append("C.{1,2}C.{5,45}[VMFLWIE].C.{1,4}C.{1,4}[WYFVQHLT]H..C.{5,45}[WFLYI].C..C")
	domaindb.append("C[KR].C...I.K...[RG].{16,18}W[FYH]H..C")
	domaindb.append("C..C.[DE].....[HN][FY]....C..C..FF.R")
	domaindb.append("[FI]S[KR]KC.[EK]RWKTM")
	domaindb.append("W[ST]..E[DE]..[LIV]")
	domaindb.append("W..[LI][SAG].{4,5}R........[YW]...[LIVM]")
	domaindb.append("LMA[EQ]GLYN")
	prosite_des = []
	prosite_des.append("'Homeobox' domain signature")
	prosite_des.append("Zinc finger C2H2 type domain signature")
	prosite_des.append("Basic-leucine zipper (bZIP) domain signature")
	prosite_des.append("'helix-loop-helix' domain signature")
	prosite_des.append("Zinc finger RING-type signature")
	prosite_des.append("Zinc finger RanBP2-type profile")
	prosite_des.append("Zinc finger MYND-type signature")
	prosite_des.append("Zinc finger PHD-type signature")
	prosite_des.append("Poly(ADP-ribose) polymerase zinc finger domain signature")
	prosite_des.append("Nuclear hormones receptors DNA-binding region signature")
	prosite_des.append("HMG box A DNA-binding domain signature")
	prosite_des.append("Myb DNA-binding domain repeat signature 1")
	prosite_des.append("Myb DNA-binding domain repeat signature 2")
	prosite_des.append("'Homeobox' engrailed-type protein signature")
	i=0
	for domain in domaindb:
		if len(re.findall(domain,sequence))>0:
			dna_associated_domain=1
			dna_associated_domain_desc=prosite_des[i]
			break
		i=i+1
	return (dna_associated_domain, dna_associated_domain_desc)

def search_pm_domain(sequence):
	pm_receptor_domain=0
	pm_receptor_domain_desc=""
	domaindb=[]
	domaindb.append("[GSTALIVMFYWC][GSTANCPDE][^EDPKRH]..[LIVMNQGA]..[LIVMFT][GSTANC][LIVMFYWSTAC][DENH]R[FYWCSH]..[LIVM]")
	domaindb.append("C...[FYWLIV].D.{3,4}C[FW]..[STAGV].{8,9}C[PF]")
	domaindb.append("QG[LMFCA][LIVMFT][LIV].[LIVFST][LIF][VFYH]C[LFY].N..V")
	domaindb.append("[LV].N[LIVM][LIVM].LF.I[PA]Q[LIVM][STA].[STA][STA][STA][STAN]")
	domaindb.append("CC[FYW].C..C....[FYW].{2,4}[DN]..[STAH]C..C")
	domaindb.append("C.[LIVMFQ].[LIVMF]..[FY]P.D...C")
	domaindb.append("[DN][LIV]Y...YYR")
	domaindb.append("G.H.N[LIVM]VNLLGACT")
	domaindb.append("F.[DN].[GAW][GA]C[LIVM][SA][LIVM][LIVM][SA][LV][KRHQ][LIVA]...[KR]C[PSAW]")
	domaindb.append("C..[DE]G[DEQKRG]W.{2,3}[PAQ][LIVMT][GT].C.C..G[HFY][EQ]")   
	domaindb.append("G...[LIVMF]..[GSA][LIVMFT][LIVMF]GC.[GA][STAP]..[EGA]..[CWN][LIVMG][LIVM]")   
	prosite_des = []
	prosite_des.append("G-protein coupled receptors family 1 signature")
	prosite_des.append("G-protein coupled receptors family 2 signature 1")
	prosite_des.append("G-protein coupled receptors family 2 signature 2")
	prosite_des.append("G-protein coupled receptors family 3 signature 1")
	prosite_des.append("G-protein coupled receptors family 3 signature 2")
	prosite_des.append("Neurotransmitter-gated ion-channels signature")
	prosite_des.append("Receptor tyrosine kinase class II signature")
	prosite_des.append("Receptor tyrosine kinase class III signature")
	prosite_des.append("Receptor tyrosine kinase class V signature 1")
	prosite_des.append("Receptor tyrosine kinase class V signature 2")
	prosite_des.append("Transmembrane 4 family signature")
	i=0
	for domain in domaindb:
		if len(re.findall(domain,sequence))>0:
			pm_receptor_domain=1
			pm_receptor_domain_desc=prosite_des[i]
			break
		i=i+1
	return (pm_receptor_domain, pm_receptor_domain_desc)


def search(data):
	
	result=[]
	proteins = util.parse_fasta_file(data)
	
	for i in range (0,len(proteins)):

		glyco_sites = 1000*(float(len(re.findall("N[^P][S|T][^P]",proteins[i]['sequence']))) /float( len(proteins[i]['sequence'])))
		nls_mono = re.findall("K[K|R].[K|R]",proteins[i]['sequence'])
		if len(nls_mono) >0:
			nls_mono = 1
		else: nls_mono = 0
		sequence = proteins[i]['sequence'] 
		er_target=re.findall("[KRHQSA][DENQ]EL$",sequence)
		if len(er_target) >0:
			er_target = 1
		else: er_target = 0	 
		peroxi_target=re.findall("[STAGCN][RKH][LIVMAFY]$",sequence)
		if len(peroxi_target) >0:
			peroxi_target = 1
		else: peroxi_target = 0
		nuclear_bipartite_list=re.findall("[KR][KR]...............",sequence)
		nuclear_bipartite=0
		for tmp in nuclear_bipartite_list:
			tmp2=re.findall(".....$",tmp)
			tmp2=tmp2[0]
			count=re.findall("[KR]",tmp2)
			if len(count)>=3:
				nuclear_bipartite=1
				break
		predictNLS = searchNLS(sequence)
		(dna_associated_domain, dna_associated_domain_desc) = search_nuc_domain(sequence)
		(pm_receptor_domain, pm_receptor_domain_desc) = search_pm_domain(sequence)
		result.append({'id':proteins[i]['id'],'nls_mono':nls_mono,'glyco_sites':glyco_sites, 'er_target':er_target,
					   'peroxi_target':peroxi_target, 'nuclear_bipartite':nuclear_bipartite,'predictNLS':predictNLS,
					   'dna_associated_domain':dna_associated_domain, 'dna_associated_domain_desc':dna_associated_domain_desc,
					   'pm_receptor_domain':pm_receptor_domain, 'pm_receptor_domain_desc':pm_receptor_domain_desc})
	return result
