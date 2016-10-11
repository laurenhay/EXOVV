#!/usr/bin/env python
from optparse import OptionParser
from jettools import getJER
from math import sqrt

parser = OptionParser()


parser.add_option('--outlabel', type='string', action='store',
                  dest='outlabel',
                  default = "responses_otherway",
                  help='Label for plots')


parser.add_option('--maxEvents', type='int', action='store',
                  dest='maxEvents',
                  default = None,
                  help='Max events')

parser.add_option('--herwigFlat', action='store_true',
                  dest='herwigFlat',
                  default = False,
                  help='Max events')

(options, args) = parser.parse_args()
argv = []

import ROOT
import array
import math
import random

ROOT.gSystem.Load("RooUnfold/libRooUnfold")

ptBinA = array.array('d', [  200., 260., 350., 460., 550., 650., 760., 900, 1000, 1100, 1200, 1300, 13000.])
nbinsPt = len(ptBinA) - 1
mBinA = array.array('d', [0, 1, 5, 10, 20, 40, 60, 80, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000])
nbinsm = len(mBinA) - 1

trueVarHist = ROOT.TH2F('truehist2d', 'truehist2D', nbinsm, mBinA, nbinsPt, ptBinA)
measVarHist = ROOT.TH2F('meashist2d', 'meashist2D', nbinsm, mBinA, nbinsPt, ptBinA)

response = ROOT.RooUnfoldResponse()
response.SetName("2d_response")
response.Setup(measVarHist, trueVarHist)

response_pdfup = ROOT.RooUnfoldResponse()
response_pdfup.SetName("2d_response_pdfup")
response_pdfup.Setup(measVarHist, trueVarHist)

response_pdfdn = ROOT.RooUnfoldResponse()
response_pdfdn.SetName("2d_response_pdfdn")
response_pdfdn.Setup(measVarHist, trueVarHist)

response_softdrop_pdfup = ROOT.RooUnfoldResponse()
response_softdrop_pdfup.SetName("2d_response_softdrop_pdfup")
response_softdrop_pdfup.Setup(measVarHist, trueVarHist)

response_softdrop_pdfdn = ROOT.RooUnfoldResponse()
response_softdrop_pdfdn.SetName("2d_response_softdrop_pdfdn")
response_softdrop_pdfdn.Setup(measVarHist, trueVarHist)

response_cteq = ROOT.RooUnfoldResponse()
response_cteq.SetName("2d_response_cteq")
response_cteq.Setup(measVarHist, trueVarHist)

response_softdrop_cteq = ROOT.RooUnfoldResponse()
response_softdrop_cteq.SetName("2d_response_softdrop_cteq")
response_softdrop_cteq.Setup(measVarHist, trueVarHist)

response_mstw = ROOT.RooUnfoldResponse()
response_mstw.SetName("2d_response_mstw")
response_mstw.Setup(measVarHist, trueVarHist)

response_softdrop_mstw = ROOT.RooUnfoldResponse()
response_softdrop_mstw.SetName("2d_response_softdrop_mstw")
response_softdrop_mstw.Setup(measVarHist, trueVarHist)

response_jecup = ROOT.RooUnfoldResponse()
response_jecup.SetName("2d_response_jecup")
response_jecup.Setup(measVarHist, trueVarHist)

response_jecdn = ROOT.RooUnfoldResponse()
response_jecdn.SetName("2d_response_jecdn")
response_jecdn.Setup(measVarHist, trueVarHist)

response_jerup = ROOT.RooUnfoldResponse()
response_jerup.SetName("2d_response_jerup")
response_jerup.Setup(measVarHist, trueVarHist)

response_jerdn = ROOT.RooUnfoldResponse()
response_jerdn.SetName("2d_response_jerdn")
response_jerdn.Setup(measVarHist, trueVarHist)

response_jernom = ROOT.RooUnfoldResponse()
response_jernom.SetName("2d_response_jernom")
response_jernom.Setup(measVarHist, trueVarHist)

response_jmrup = ROOT.RooUnfoldResponse()
response_jmrup.SetName("2d_response_jmrup")
response_jmrup.Setup(measVarHist, trueVarHist)

response_jmrdn = ROOT.RooUnfoldResponse()
response_jmrdn.SetName("2d_response_jmrdn")
response_jmrdn.Setup(measVarHist, trueVarHist)

response_jmrnom = ROOT.RooUnfoldResponse()
response_jmrnom.SetName("2d_response_jmrnom")
response_jmrnom.Setup(measVarHist, trueVarHist)

response_softdrop = ROOT.RooUnfoldResponse()
response_softdrop.SetName("2d_response_softdrop")
response_softdrop.Setup(measVarHist, trueVarHist)


response_softdrop_jecup = ROOT.RooUnfoldResponse()
response_softdrop_jecup.SetName("2d_response_softdrop_jecup")
response_softdrop_jecup.Setup(measVarHist, trueVarHist)

response_softdrop_jecdn = ROOT.RooUnfoldResponse()
response_softdrop_jecdn.SetName("2d_response_softdrop_jecdn")
response_softdrop_jecdn.Setup(measVarHist, trueVarHist)

response_softdrop_jerup = ROOT.RooUnfoldResponse()
response_softdrop_jerup.SetName("2d_response_softdrop_jerup")
response_softdrop_jerup.Setup(measVarHist, trueVarHist)

response_softdrop_jerdn = ROOT.RooUnfoldResponse()
response_softdrop_jerdn.SetName("2d_response_softdrop_jerdn")
response_softdrop_jerdn.Setup(measVarHist, trueVarHist)

response_softdrop_jernom = ROOT.RooUnfoldResponse()
response_softdrop_jernom.SetName("2d_response_softdrop_jernom")
response_softdrop_jernom.Setup(measVarHist, trueVarHist)

response_softdrop_jmrup = ROOT.RooUnfoldResponse()
response_softdrop_jmrup.SetName("2d_response_softdrop_jmrup")
response_softdrop_jmrup.Setup(measVarHist, trueVarHist)

response_softdrop_jmrdn = ROOT.RooUnfoldResponse()
response_softdrop_jmrdn.SetName("2d_response_softdrop_jmrdn")
response_softdrop_jmrdn.Setup(measVarHist, trueVarHist)

response_softdrop_jmrnom = ROOT.RooUnfoldResponse()
response_softdrop_jmrnom.SetName("2d_response_softdrop_jmrnom")
response_softdrop_jmrnom.Setup(measVarHist, trueVarHist)

h_2DHisto_meas = ROOT.TH2F('PFJet_pt_m_AK8', 'HLT Binned Mass and P_{T}; P_{T} (GeV); Mass (GeV)', nbinsm, mBinA, nbinsPt, ptBinA)
h_2DHisto_gen = ROOT.TH2F('PFJet_pt_m_AK8Gen', 'Generator Mass vs. P_{T}; P_{T} (GeV); Mass (GeV)', nbinsm, mBinA, nbinsPt, ptBinA)

h_2DHisto_measSD = ROOT.TH2F('PFJet_pt_m_AK8SD', 'HLT Binned Mass and P_{T}; P_{T} (GeV); Mass (GeV)', nbinsm, mBinA, nbinsPt, ptBinA)
h_2DHisto_genSD = ROOT.TH2F('PFJet_pt_m_AK8SDgen', 'Generator Mass and P_{T}; P_{T} (GeV); Mass (GeV)', nbinsm, mBinA, nbinsPt, ptBinA)


h_pt_meas = ROOT.TH1F("h_pt_meas", ";Jet p_{T} (GeV); Number", 150, 0, 3000)
h_y_meas = ROOT.TH1F("h_y_meas", ";Jet Rapidity; Number", 50, -2.5, 2.5 )
h_phi_meas = ROOT.TH1F("h_phi_meas", ";Jet #phi (radians); Number", 50, -ROOT.TMath.Pi(), ROOT.TMath.Pi() )
h_m_meas = ROOT.TH1F("h_m_meas", ";Jet Mass (GeV); Number", 50, 0, 500 )
h_msd_meas = ROOT.TH1F("h_msd_meas", ";Jet Soft Drop Mass (GeV); Number", 50, 0, 500 )
h_rho_meas = ROOT.TH1F("h_rho_meas", ";Jet (m/p_{T}R)^{2}; Number", 100, 0, 1.0 )
h_tau21_meas = ROOT.TH1F("h_tau21_meas", ";Jet #tau_{2}/#tau_{1}; Number", 50, 0, 1.0 )
h_dphi_meas = ROOT.TH1F("h_dphi_meas", ";Jet #phi (radians); Number", 50, 0, ROOT.TMath.TwoPi() )
h_ptasym_meas = ROOT.TH1F("h_ptasym_meas", ";Jet (p_{T1} - p_{T2}) / (p_{T1} + p_{T2}); Number", 50, 0, 1.0 )
h_rho_vs_tau_meas = ROOT.TH2F("h_rho_vs_tau21_meas", ";Jet (m/p_{T}R)^{2};Jet #tau_{2}/#tau_{1}", 100, 0, 1.0, 50, 0, 1.0 )

h_massup = ROOT.TH1F("h_massup", "JMR Up Variation", nbinsm, mBinA)
h_massdn = ROOT.TH1F("h_massdn", "JMR Down Variation", nbinsm, mBinA)
h_massnom = ROOT.TH1F("h_massnom", "JMR Nominal", nbinsm, mBinA)

h_massup_softdrop = ROOT.TH1F("h_massup_softdrop", "JMR Up Softdrop", nbinsm, mBinA)
h_massdn_softdrop = ROOT.TH1F("h_massdn_softdrop", "JMR Down Softdrop", nbinsm, mBinA)
h_massnom_softdrop = ROOT.TH1F("h_massnom_softdrop", "JMR Nominal Softdrop", nbinsm, mBinA)

h_mreco_mgen = ROOT.TH1F("h_mreco_mgen", "Reco Mass/Gen Mass", 1000, 0, 2)
h_ptreco_ptgen = ROOT.TH1F("h_ptreco_ptgen", "Reco Pt/Gen Pt", 1000, 0, 2)
h_mreco_mgen_softdrop = ROOT.TH1F("h_mreco_mgen_softdrop", "Reco Mass/Gen Mass Softdrop", 1000, 0, 2)
h_ptreco_ptgen_softdrop = ROOT.TH1F("h_ptreco_ptgen_softdrop", "Reco Pt/Gen Pt Softdrop", 1000, 0, 2)


def getMatched( p4, coll, dRMax = 0.1) :
    if coll != None : 
        for i,c in enumerate(coll):
            if p4.DeltaR(c) < dRMax :
                return i
    return None



ROOT.gStyle.SetOptStat(000000)
#ROOT.gROOT.Macro("rootlogon.C")
#ROOT.gStyle.SetPadRightMargin(0.15)
ROOT.gStyle.SetOptStat(000000)
ROOT.gStyle.SetTitleFont(43)
#ROOT.gStyle.SetTitleFontSize(0.05)
ROOT.gStyle.SetTitleFont(43, "XYZ")
ROOT.gStyle.SetTitleSize(30, "XYZ")
#ROOT.gStyle.SetTitleOffset(3.5, "X")
ROOT.gStyle.SetLabelFont(43, "XYZ")
ROOT.gStyle.SetLabelSize(24, "XYZ")


deweightFlat = False

if not options.herwigFlat : 
    qcdIn =[
        ROOT.TFile('qcdpy8_170to300_repdf.root'),
        ROOT.TFile('qcdpy8_300to470_repdf.root'),
        ROOT.TFile('qcdpy8_470to600_repdf.root'),
        ROOT.TFile('qcdpy8_600to800_repdf.root'),
        ROOT.TFile('qcdpy8_800to1000_repdf.root'),
        ROOT.TFile('qcdpy8_1000to1400_repdf.root'),
        ROOT.TFile('qcdpy8_1400to1800_repdf.root'),
        ROOT.TFile('qcdpy8_1800to2400_repdf.root'),
        ROOT.TFile('qcdpy8_2400to3200_repdf.root'),
        ROOT.TFile('qcdpy8_3200toinf_repdf.root'),
        ]
    qcdWeights =[
        117276.      / 6918748.,  #170to300    
        7823.        / 5968960.,  #300to470    
        648.2        / 3977770.,  #470to600    
        186.9        / 3979884.,  #600to800    
        32.293       / 3973224.,  #800to1000   
        9.4183       / 2953982.,  #1000to1400  
        0.84265      / 395725. ,  #1400to1800  
        0.114943     / 393760. ,  #1800to2400  
        0.00682981   / 398452. ,  #2400to3200  
        0.000165445  / 391108. ,  #3200toInf   
        ]
else : 
    qcdIn =[
        ROOT.TFile('qcd_ptflat_herwig.root'),
        ]
    qcdWeights =[
        1.0
        ]
    deweightFlat = True
        
masslessSD = 0


trees = []
# Append the actual TTrees
for iq in qcdIn:
    trees.append( iq.Get("TreeEXOVV") )
fout = ROOT.TFile(options.outlabel + '_qcdmc.root', 'RECREATE')


for itree,t in enumerate(trees) :
    Weight = array.array('f', [-1])    
    NFatJet = array.array('i', [0] )
    
    NNPDF3weight_CorrDn = array.array('f', [-1.])
    NNPDF3weight_CorrUp = array.array('f', [-1.])


    CTEQweight_Central = array.array('f', [-1.])
    MSTWweight_Central = array.array('f', [-1.])

    
    FatJetPt = array.array('f', [-1]*5)
    FatJetEta = array.array('f', [-1]*5)
    FatJetRap = array.array('f', [-1]*5)
    FatJetPhi = array.array('f', [-1]*5)
    FatJetMass = array.array('f', [-1]*5)
    FatJetMassSoftDrop = array.array('f', [-1]*5)
    FatJetTau21 = array.array('f', [-1]*5)
    FatJetCorrUp = array.array('f', [-1]*5)
    FatJetCorrDn = array.array('f', [-1]*5)
    FatJetRhoRatio = array.array('f', [-1]*5)
    NGenJet = array.array('i', [0] )
    GenJetPt = array.array('f', [-1]*5)
    GenJetEta = array.array('f', [-1]*5)
    GenJetPhi = array.array('f', [-1]*5)
    GenJetMass = array.array('f', [-1]*5)
    GenJetMassSoftDrop = array.array('f', [-1]*5)
    GenJetRhoRatio = array.array('f', [-1]*5)
    FatJetPtSoftDrop = array.array('f', [-1]*5)
    GenJetPtSoftDrop = array.array('f', [-1]*5)
    
    
    Trig = array.array('i', [-1] )
    
    t.SetBranchStatus ('*', 0)
    t.SetBranchStatus ('Weight', 1)
    t.SetBranchStatus ('NFatJet', 1)
    t.SetBranchStatus ('NGenJet', 1)
    t.SetBranchStatus ('FatJetPt', 1)
    t.SetBranchStatus ('FatJetEta', 1)
    t.SetBranchStatus ('FatJetRap', 1)
    t.SetBranchStatus ('FatJetPhi', 1)
    t.SetBranchStatus ('FatJetMass', 1)
    t.SetBranchStatus ('FatJetMassSoftDrop', 1)
    t.SetBranchStatus ('GenJetPt', 1)
    t.SetBranchStatus ('GenJetEta', 1)
    t.SetBranchStatus ('GenJetPhi', 1)
    t.SetBranchStatus ('GenJetMass', 1)
    t.SetBranchStatus ('GenJetMassSoftDrop', 1)    
    t.SetBranchStatus ('FatJetRhoRatio', 1)
    t.SetBranchStatus ('FatJetTau21', 1)
    t.SetBranchStatus ('FatJetCorrUp', 1)
    t.SetBranchStatus ('FatJetCorrDn', 1)
    t.SetBranchStatus ('Trig', 1)
    t.SetBranchStatus ('GenJetRhoRatio', 1)
    t.SetBranchStatus ('GenJetPtSoftDrop', 1)
    t.SetBranchStatus ('FatJetPtSoftDrop', 1)
    t.SetBranchStatus ('NNPDF3weight_CorrDn', 1)
    t.SetBranchStatus ('NNPDF3weight_CorrUp', 1)    

    t.SetBranchStatus ('CTEQweight_Central', 1)
    t.SetBranchStatus ('MSTWweight_Central', 1)


    t.SetBranchAddress ('NNPDF3weight_CorrDn', NNPDF3weight_CorrDn)
    t.SetBranchAddress ('NNPDF3weight_CorrUp', NNPDF3weight_CorrUp)
    t.SetBranchAddress ('CTEQweight_Central', CTEQweight_Central)
    t.SetBranchAddress ('MSTWweight_Central', MSTWweight_Central)
    t.SetBranchAddress ('Weight', Weight)
    t.SetBranchAddress ('NFatJet', NFatJet)
    t.SetBranchAddress ('NGenJet', NGenJet)
    t.SetBranchAddress ('FatJetPt', FatJetPt)
    t.SetBranchAddress ('FatJetEta', FatJetEta)
    t.SetBranchAddress ('FatJetRap', FatJetRap)
    t.SetBranchAddress ('FatJetPhi', FatJetPhi)
    t.SetBranchAddress ('FatJetMass', FatJetMass)
    t.SetBranchAddress ('FatJetMassSoftDrop', FatJetMassSoftDrop)
    t.SetBranchAddress ('FatJetCorrUp', FatJetCorrUp)
    t.SetBranchAddress ('FatJetCorrDn', FatJetCorrDn)
    t.SetBranchAddress ('GenJetPt', GenJetPt)
    t.SetBranchAddress ('GenJetEta', GenJetEta)
    t.SetBranchAddress ('GenJetPhi', GenJetPhi)
    t.SetBranchAddress ('GenJetMass', GenJetMass)
    t.SetBranchAddress ('GenJetMassSoftDrop', GenJetMassSoftDrop)
    t.SetBranchAddress ('FatJetRhoRatio', FatJetRhoRatio)
    t.SetBranchAddress ('FatJetTau21', FatJetTau21)
    t.SetBranchAddress ('Trig', Trig)
    t.SetBranchAddress ('GenJetRhoRatio', GenJetRhoRatio)
    t.SetBranchAddress ('FatJetPtSoftDrop', FatJetPtSoftDrop)
    t.SetBranchAddress ('GenJetPtSoftDrop', GenJetPtSoftDrop)
    entries = t.GetEntriesFast()
    print 'Processing tree ' + str(itree)
    

    if options.maxEvents != None :
        eventsToRun = options.maxEvents
    else :
        eventsToRun = entries
    for jentry in xrange( eventsToRun ):
        if jentry % 10000 == 0 :
            print 'processing ' + str(jentry)
        # get the next tree in the chain and verify
        ientry = t.GetEntry( jentry )
        if ientry < 0:
            break

        GenJets = []
        FatJets = []
        GenJetsMassSD = []
        FatJetsMassSD = []        
        GenJetsSD = []
        FatJetsSD = []
        weight = qcdWeights[itree]


        if NFatJet[0] < 2 : 
            continue

        pttuple = [ ]
        for ijet in xrange( NFatJet[0] ) : 
            pttuple.append( [ijet, FatJetPt[ijet] ] )


        pttuplesorted = sorted(pttuple, key=lambda ptsort : ptsort[1], reverse=True )
                           

        maxjet = pttuplesorted[0][0]
        minjet = pttuplesorted[1][0]

        #print pttuplesorted
        #print maxjet, ' ', minjet


        ptasym = (FatJetPt[maxjet] - FatJetPt[minjet])/(FatJetPt[maxjet] + FatJetPt[minjet])
        dphi = ROOT.TVector2.Phi_0_2pi( FatJetPhi[maxjet] - FatJetPhi[minjet] )


        if deweightFlat != None and deweightFlat :
            weight *= Weight[0]

            if 5e-6 < weight/(FatJetPt[maxjet]+FatJetPt[minjet]):
                continue
            

        
        pdfweight_up = NNPDF3weight_CorrUp[0]
        pdfweight_dn = NNPDF3weight_CorrDn[0]
        cteqweight = CTEQweight_Central[0]
        mstwweight = MSTWweight_Central[0]
        #print "pdfweight up: " + str(pdfweight_up)
        #print "pdfweight down: " + str(pdfweight_dn)
        #print 'cteq weight: ' + str(cteqweight)
        #print 'mstw weight: ' + str(mstwweight)



        # We want two kinematic selections:
        # 1. "Loose" selection for the response matrix to handle migration effects.
        # 2. Full selection for the filled histograms for data/MC comparisons and unfolding closure, etc.
        passkinfull = FatJetPt[minjet] > 220. 
                
        if dphi > 1.57 and passkinfull :
            h_ptasym_meas.Fill( ptasym, weight )
        if ptasym < 0.3 and passkinfull :
            h_dphi_meas.Fill( dphi, weight )

        passkinloose = ptasym < 0.3 and dphi > 1.57 and dphi < 4.71
        if not passkinloose :
            continue


        
        for igen in xrange( int(NGenJet[0]) ):
            GenJet = ROOT.TLorentzVector()
            GenJet.SetPtEtaPhiM( GenJetPt[igen], GenJetEta[igen], GenJetPhi[igen], GenJetMass[igen])
            GenJetSD = ROOT.TLorentzVector()
            GenJetSD.SetPtEtaPhiM( GenJetPtSoftDrop[igen], GenJetEta[igen], GenJetPhi[igen], GenJetMassSoftDrop[igen] )
            GenJets.append(GenJet)
            GenJetsSD.append(GenJetSD)
            GenJetsMassSD.append( GenJetMassSoftDrop[igen] )            
            h_2DHisto_gen.Fill( GenJet.M(), GenJet.Perp(), weight )
            h_2DHisto_genSD.Fill( GenJetSD.M(), GenJetSD.Perp(), weight)
        # First get the "Fills" and "Fakes" (i.e. we at least have a RECO jet)
        for ijet in [maxjet, minjet]:
            
            FatJet = ROOT.TLorentzVector()
            FatJet.SetPtEtaPhiM( FatJetPt[ijet], FatJetEta[ijet], FatJetPhi[ijet], FatJetMass[ijet])
            
            FatJetSD = ROOT.TLorentzVector()
            FatJetSD.SetPtEtaPhiM( FatJetPtSoftDrop[ijet], FatJetEta[ijet], FatJetPhi[ijet], FatJetMassSoftDrop[ijet]  )
            
            FatJetsSD.append(FatJetSD)
            FatJets.append(FatJet)

            if passkinfull : 
                h_2DHisto_meas.Fill( FatJet.M(), FatJet.Perp(),  weight )
                h_2DHisto_measSD.Fill( FatJetSD.M(), FatJetSD.Perp(),  weight)

            igen = getMatched( FatJet, GenJets )
            igenSD = getMatched(FatJetSD, GenJetsSD, dRMax=0.5)
            
          
            if igen != None :  # Here we have a "Fill"

                
                valup = getJER(FatJet.Eta(), +1) #JER nominal=0, up=+1, down=-1
                recopt = FatJet.Perp()
                genpt = GenJets[igen].Perp()
                deltapt = (recopt-genpt)*(valup-1.0)
                if abs(recopt) > 0.0 : smearup = max(0.0, (recopt+deltapt)/recopt)
                else : smearup = 0.0
                
                valdn = getJER(FatJet.Eta(), -1) #JER nominal=0, dn=+1, down=-1
                recopt = FatJet.Perp()
                genpt = GenJets[igen].Perp()
                deltapt = (recopt-genpt)*(valdn-1.0)
                if abs(recopt) > 0.0 : smeardn = max(0.0, (recopt+deltapt)/recopt)
                else : smeardn = 0.0
                                                
                valnom = getJER(FatJet.Eta(), 0)
                recopt = FatJet.Perp()
                genpt = GenJets[igen].Perp()
                deltapt = (recopt-genpt)*(valnom-1.0)
                if abs(recopt) > 0.0 : smearnom = max(0.0, (recopt+deltapt)/recopt)
                else : smearnom = 0.
                
                jmrvalup = 1.2
                recomass = FatJet.M()
                genmass = GenJets[igen].M()
                deltamass = (recomass-genmass)*(jmrvalup-1.0)
                if abs(recomass) > 0.0 : jmrup = max(0.0, (recomass+deltamass)/recomass)
                else : jmrup = 0.
                
                jmrvaldn = 1.0
                recomass = FatJet.M()
                genmass = GenJets[igen].M()
                deltamass = (recomass-genmass)*(jmrvaldn-1.0)
                if abs(recomass) > 0.0 : jmrdn = max(0.0, (recomass+deltamass)/recomass)
                else : jmrdn = 0.

                jmrvalnom = 1.1
                recomass = FatJet.M()
                genmass = GenJets[igen].M()
                deltamass = (recomass-genmass)*(jmrvalnom-1.0)
                if abs(recomass) > 0.0 : jmrnom = max(0.0, (recomass+deltamass)/recomass)
                else : jmrnom = 0.


                response.Fill( FatJet.M(), FatJet.Perp(), GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jecup.Fill( FatJet.M() * FatJetCorrUp[ijet], FatJet.Perp()* FatJetCorrUp[ijet], GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jecdn.Fill( FatJet.M() * FatJetCorrDn[ijet], FatJet.Perp()* FatJetCorrDn[ijet], GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jerup.Fill( FatJet.M() * smearup, FatJet.Perp()* smearup, GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jerdn.Fill( FatJet.M() * smeardn, FatJet.Perp()* smeardn, GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jernom.Fill(FatJet.M() * smearnom, FatJet.Perp()*smearnom, GenJets[igen].M(), GenJets[igen].Perp(), weight)
                
                response_jmrup.Fill( FatJet.M(), FatJet.Perp()*jmrup, GenJets[igen].M(), GenJets[igen].Perp(), weight)
                response_jmrdn.Fill( FatJet.M(), FatJet.Perp()*jmrdn, GenJets[igen].M(), GenJets[igen].Perp(), weight)
                response_jmrnom.Fill(FatJet.M(), FatJet.Perp()*jmrnom, GenJets[igen].M(), GenJets[igen].Perp(), weight)

                if passkinfull : 
                    h_massup.Fill(FatJet.M()*jmrup, weight)
                    h_massdn.Fill(FatJet.M()*jmrdn, weight)
                    h_massnom.Fill(FatJet.M()*jmrnom, weight)

                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_pdfup.Fill( FatJet.M(), FatJet.Perp(), GenJets[igen].M(), GenJets[igen].Perp(), weight*pdfweight_up)
                    response_pdfdn.Fill( FatJet.M(), FatJet.Perp(), GenJets[igen].M(), GenJets[igen].Perp(), weight*pdfweight_dn)

                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_cteq.Fill( FatJet.M(), FatJet.Perp(), GenJets[igen].M(), GenJets[igen].Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_mstw.Fill( FatJet.M(), FatJet.Perp(), GenJets[igen].M(), GenJets[igen].Perp(), weight*mstwweight)


                # Make some data-to-MC plots

                #                h_2DHisto_meas.Fill( FatJetPt[ijet], FatJetMass[ijet], weight )
                if passkinfull : 

                    h_pt_meas.Fill( FatJetPt[ijet] , weight )
                    h_y_meas.Fill( FatJetRap[ijet] , weight )
                    h_phi_meas.Fill( FatJetPhi[ijet] , weight )
                    h_m_meas.Fill( FatJetMass[ijet] , weight )
                    h_rho_meas.Fill( FatJetRhoRatio[ijet] , weight )
                    h_tau21_meas.Fill( FatJetTau21[ijet] , weight )
                    h_rho_vs_tau_meas.Fill( FatJetRhoRatio[ijet], FatJetTau21[ijet] , weight )
                    if GenJets[igen].M() != 0:
                        h_mreco_mgen.Fill(FatJet.M()/GenJets[igen].M(), weight)
                    else:
                        h_mreco_mgen.Fill(FatJet.M()/0.140, weight)
                    h_ptreco_ptgen.Fill(FatJet.Perp()/GenJets[igen].Perp(), weight)        
            else : # Here we have a "Fake"
                response.Fake( FatJet.M(), FatJet.Perp(), weight )
                response_jecup.Fake( FatJet.M() * FatJetCorrUp[ijet], FatJet.Perp()* FatJetCorrUp[ijet], weight )
                response_jecdn.Fake( FatJet.M() * FatJetCorrDn[ijet], FatJet.Perp()* FatJetCorrDn[ijet], weight )
                response_jerup.Fake( FatJet.M() * smearup, FatJet.Perp() * smearup, weight )
                response_jerdn.Fake( FatJet.M() * smeardn, FatJet.Perp() * smeardn, weight ) 
                response_jernom.Fake(FatJet.M() * smearnom, FatJet.Perp() * smearnom,weight)
                response_jmrup.Fake( FatJet.M(), FatJet.Perp()*jmrup, weight)
                response_jmrnom.Fake(FatJet.M(), FatJet.Perp()*jmrnom, weight)
                response_jmrdn.Fake( FatJet.M(), FatJet.Perp()*jmrdn, weight)

                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_pdfup.Fake(FatJet.M(), FatJet.Perp(), weight*pdfweight_up)
                    response_pdfdn.Fake(FatJet.M(), FatJet.Perp(), weight*pdfweight_dn)

                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_cteq.Fake( FatJet.M(), FatJet.Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_mstw.Fake( FatJet.M(), FatJet.Perp(), weight*mstwweight)


            if igenSD != None:
                
                #### be less conservative, define jes and jer for SD now
                valupSD = getJER(FatJetSD.Eta(), +1)
                recoptSD = FatJetSD.Perp()
                genptSD = GenJetsSD[igenSD].Perp()
                deltaptSD = (recoptSD-genptSD)*(valupSD-1.0)
                if abs(recoptSD) > 0.0 : smearupSD = max(0.0, (recoptSD+deltaptSD)/recoptSD)
                else : smearupSD = 0.
        
                valdnSD = getJER(FatJetSD.Eta(), -1)
                recoptSD = FatJetSD.Perp()
                genptSD = GenJetsSD[igenSD].Perp()
                deltaptSD = (recoptSD-genptSD)*(valdnSD-1.0)
                if abs(recoptSD) > 0.0 : smeardnSD = max(0.0, (recoptSD+deltaptSD)/recoptSD)
                else : smeardnSD = 0.

                valnomSD = getJER(FatJetSD.Eta(), 0)
                recoptSD = FatJetSD.Perp()
                genptSD = GenJetsSD[igenSD].Perp()
                deltaptSD = (recoptSD-genptSD)*(valnomSD-1.0)
                if abs(recoptSD) > 0.0 : smearnomSD = max(0.0, (recoptSD+deltaptSD)/recoptSD)
                else : smearnomSD = 0.
        
                jmrvalnomSD = 1.1
                recomassSD = FatJetSD.M()
                genmassSD = GenJetsSD[igenSD].M()
                deltamassSD = (recomassSD-genmassSD)*(jmrvalnomSD-1.0)
                if abs(recomassSD) > 0.0 : jmrnomSD = max(0.0, (recomassSD+deltamassSD)/recomassSD)
                else : jmrnomSD = 0.
  
                jmrvalupSD = 1.2
                recomassSD = FatJetSD.M()
                genmassSD = GenJetsSD[igenSD].M()
                deltamassSD = (recomassSD-genmassSD)*(jmrvalupSD-1.0)
                if abs(recomassSD) > 0.0 : jmrupSD = max(0.0, (recomassSD+deltamassSD)/recomassSD)
                else : jmrupSD = 0.

                jmrvaldnSD = 1.0
                recomassSD = FatJetSD.M()
                genmassSD = GenJetsSD[igenSD].M()
                deltamassSD = (recomassSD-genmassSD)*(jmrvaldnSD-1.0)
                if abs(recomassSD) > 0.0 : jmrdnSD = max(0.0, (recomassSD+deltamassSD)/recomassSD)
                else : jmrdnSD = 0.

                response_softdrop.Fill( FatJetSD.M() , FatJetSD.Perp(), GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jecup.Fill( FatJetSD.M()  * FatJetCorrUp[ijet], FatJetSD.Perp() * FatJetCorrUp[ijet], GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jecdn.Fill( FatJetSD.M()  * FatJetCorrDn[ijet], FatJetSD.Perp() * FatJetCorrDn[ijet], GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jerup.Fill( FatJetSD.M()  * smearupSD, FatJetSD.Perp() * smearupSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jerdn.Fill( FatJetSD.M()  * smeardnSD, FatJetSD.Perp() * smeardnSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jernom.Fill(FatJetSD.M() * smearnomSD, FatJetSD.Perp() * smearnomSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                response_softdrop_jmrnom.Fill(FatJetSD.M(), FatJetSD.Perp()*jmrnomSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                response_softdrop_jmrup.Fill(FatJetSD.M(), FatJetSD.Perp()*jmrupSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                response_softdrop_jmrdn.Fill(FatJetSD.M(), FatJetSD.Perp()*jmrdnSD, GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)

                if passkinfull : 
                    h_massup_softdrop.Fill(FatJetSD.M()*jmrupSD, weight)
                    h_massdn_softdrop.Fill(FatJetSD.M()*jmrdnSD, weight)
                    h_massnom_softdrop.Fill(FatJetSD.M()*jmrnomSD, weight)
                    if GenJetsSD[igenSD].M() != 0:
                        h_mreco_mgen_softdrop.Fill(FatJetSD.M()/GenJetsSD[igenSD].M(), weight)
                    else:
                        h_mreco_mgen_softdrop.Fill(FatJetSD.M()/0.14, weight)
                        masslessSD += 1
                    h_ptreco_ptgen_softdrop.Fill(FatJetSD.Perp()/GenJetsSD[igenSD].Perp(), weight)
                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_softdrop_pdfup.Fill( FatJetSD.M(), FatJetSD.Perp(), GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*pdfweight_up)
                    response_softdrop_pdfdn.Fill( FatJetSD.M(), FatJetSD.Perp(), GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*pdfweight_dn)


                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_softdrop_cteq.Fill( FatJetSD.M(), FatJetSD.Perp(), GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_softdrop_mstw.Fill( FatJetSD.M(), FatJetSD.Perp(), GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*mstwweight)


                if passkinfull: 
                    h_msd_meas.Fill( FatJetMassSoftDrop[ijet] , weight )
 #               h_2DHisto_measSD.Fill( FatJetPt[ijet], FatJetMassSoftDrop[ijet], weight )
            else:
                response_softdrop.Fake( FatJetSD.M() , FatJetSD.Perp(), weight )
                response_softdrop_jecup.Fake( FatJetSD.M()  * FatJetCorrUp[ijet], FatJetSD.Perp() * FatJetCorrUp[ijet], weight )
                response_softdrop_jecdn.Fake( FatJetSD.M()  * FatJetCorrDn[ijet], FatJetSD.Perp() * FatJetCorrDn[ijet], weight )
                response_softdrop_jerup.Fake( FatJetSD.M()  * smearupSD, FatJetSD.Perp() * smearupSD, weight )
                response_softdrop_jerdn.Fake( FatJetSD.M()  * smeardnSD, FatJetSD.Perp() * smeardnSD, weight )
                response_softdrop_jernom.Fake(FatJetSD.M() * smearnomSD, FatJetSD.Perp() * smearnomSD, weight)            
                response_softdrop_jmrnom.Fake(FatJetSD.M(), FatJetSD.Perp()*jmrnomSD, weight)
                response_softdrop_jmrup.Fake(FatJetSD.M(), FatJetSD.Perp()*jmrupSD, weight)
                response_softdrop_jmrdn.Fake(FatJetSD.M(), FatJetSD.Perp()*jmrdnSD, weight)
                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_softdrop_pdfup.Fake( FatJetSD.M(), FatJetSD.Perp(), weight*pdfweight_up)
                    response_softdrop_pdfdn.Fake( FatJetSD.M(), FatJetSD.Perp(), weight*pdfweight_dn)


                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_softdrop_cteq.Fake( FatJetSD.M(), FatJetSD.Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_softdrop_mstw.Fake( FatJetSD.M(), FatJetSD.Perp(), weight*mstwweight)

                
        # Now get the "Misses" (i.e. we have no RECO jet)
        for igen in xrange( int(NGenJet[0]) ):
            ijet = getMatched( GenJets[igen], FatJets )
            ijetSD = getMatched( GenJetsSD[igen], FatJetsSD, dRMax=0.5 )
            if ijet == None :
                response.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jecup.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jecdn.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jerup.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jerdn.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight )
                response_jernom.Miss(GenJets[igen].M(), GenJets[igen].Perp(), weight)
                response_jmrnom.Miss(GenJets[igen].M(), GenJets[igen].Perp(), weight)
                response_jmrup.Miss(GenJets[igen].M(), GenJets[igen].Perp(), weight)
                response_jmrdn.Miss(GenJets[igen].M(), GenJets[igen].Perp(), weight)
                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_pdfup.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight*pdfweight_up)
                    response_pdfdn.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight*pdfweight_dn)


                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_cteq.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_mstw.Miss( GenJets[igen].M(), GenJets[igen].Perp(), weight*mstwweight)


                    
            if ijetSD == None and igenSD != None :
                response_softdrop.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jecup.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jecdn.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jerup.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jerdn.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jernom.Miss(GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight )
                response_softdrop_jmrnom.Miss(GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                response_softdrop_jmrup.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                response_softdrop_jmrdn.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight)
                if pdfweight_up > 1.2 or pdfweight_dn < 0.8:
                    pass
                else:
                    response_softdrop_pdfup.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*pdfweight_up)
                    response_softdrop_pdfdn.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*pdfweight_dn)

                if cteqweight > 1.2 or cteqweight < 0.8:
                    pass
                else:
                    response_softdrop_cteq.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*cteqweight)
                    
                if mstwweight > 1.2 or mstwweight < 0.8:
                    pass
                else:
                    response_softdrop_mstw.Miss( GenJetsSD[igenSD].M(), GenJetsSD[igenSD].Perp(), weight*mstwweight)


                    
print "Number of Massless Softdrop Jets: " + str(masslessSD)
fout.cd()
#response.Hresponse().Draw()
response.Write()
response_jecup.Write()
response_jecdn.Write()
response_jerup.Write()
response_jerdn.Write()
h_2DHisto_gen.Write()
h_2DHisto_meas.Write()
response_jmrup.Write()
response_jmrdn.Write()
response_jmrnom.Write()
response_jernom.Write()


response_pdfup.Write()
response_pdfdn.Write()
response_softdrop_pdfup.Write()
response_softdrop_pdfdn.Write()

response_cteq.Write()
response_softdrop_cteq.Write()

response_mstw.Write()
response_softdrop_mstw.Write()

h_mreco_mgen.Write()
h_ptreco_ptgen.Write()
h_mreco_mgen_softdrop.Write()
h_ptreco_ptgen_softdrop.Write()


h_2DHisto_measSD.Write()
h_2DHisto_genSD.Write()
response_softdrop.Write()
response_softdrop_jecup.Write()
response_softdrop_jecdn.Write()
response_softdrop_jerup.Write()
response_softdrop_jerdn.Write()
response_softdrop_jmrup.Write()
response_softdrop_jmrdn.Write()
response_softdrop_jmrnom.Write()
response_softdrop_jernom.Write()

h_pt_meas.Write()
h_y_meas.Write()
h_phi_meas.Write()
h_m_meas.Write()
h_msd_meas.Write()
h_rho_meas.Write()
h_tau21_meas.Write()
h_dphi_meas.Write()
h_ptasym_meas.Write()
h_rho_vs_tau_meas.Write()

fout.Close()
