#! /usr/bin/env python

##################
# Finding the mistag rate plots
##################

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--file', type='string', action='store',
                  dest='file',
                  default = 'exovv_jetht_alltrigs.root',
                  help='Input file')



parser.add_option('--dir', type='string', action='store',
                  dest='dir',
                  default = "exovvhists",
                  help='Directory containing root histograms')



parser.add_option('--outname', type='string', action='store',
                  dest='outname',
                  default = "",
                  help='output identifier for png and pdf files')


parser.add_option('--rebin', type='int', action='store',
                  dest='rebin',
                  default = None,
                  help='Rebin if desired')




parser.add_option('--signalTrigs', action='store_true',
                  dest='signalTrigs',
                  default = False,
                  help='Use only signal triggers')



(options, args) = parser.parse_args()
argv = []


#FWLITE STUFF
import math
import ROOT
import sys
ROOT.gROOT.Macro("rootlogon.C")


f = ROOT.TFile(options.dir + '/' + options.file)

if not options.signalTrigs : 
    trigs = [
        #'HLT_PFJet80',
        #'HLT_PFJet140',
        'HLT_PFJet200',
        'HLT_PFJet260',
        'HLT_PFJet320',
        'HLT_PFJet400',
        'HLT_PFJet450',
        'HLT_PFJet500' 
        ]
    scales = [
        #30000,
        #2000,
        66,
        12,
        4,
        1,
        1,
        1
        ]
else :
    trigs = [
        'HLT_PFHT800'
        ]

    scales = [
        1 
        ]
colors1 = [ ROOT.kBlack, ROOT.kRed, ROOT.kGreen, ROOT.kBlue, ROOT.kCyan, ROOT.kMagenta, ROOT.kOrange, ROOT.kMagenta    ]
#colors = [ ROOT.kWhite, ROOT.kRed, ROOT.kGreen, ROOT.kBlue, ROOT.kCyan ]

colors2 = [ ROOT.kWhite, ROOT.kRed - 10, ROOT.kRed - 9, ROOT.kRed - 7, ROOT.kRed - 4, ROOT.kRed, ROOT.kRed + 1, ROOT.kRed + 2   ]

logy = [ True, True, False, True, True, True, True, True, True, False, False ]
palette = [0, 2]


if not options.signalTrigs : 
    hists = ['h2_pt0', 'h2_ptAK8', 'h2_yAK8', 'h2_mAK8', 'h2_msoftdropAK8', 'h2_rho_all']
    titles = [
        'Leading AK8 Jet p_{T};p_{T} (GeV)',
        'AK8 p_{T};p_{T} (GeV)',
        'AK8 Rapidity;y',
        'AK8 ungroomed mass;Mass (GeV)',
        'AK8 soft-drop mass, z_{cut}=0.1, #beta=0;Mass (GeV)',
        'AK8 Jet #rho = (m/p_{T}R)^{2};#rho',
        #'AK8 #tau_{21} = #tau_{2} / #tau_{1};#tau_{21}',
        #'AK8 #Delta R between subjets;#Delta R',
        #'AK8 Jet Fragmentation z = min(p_{T}^{i}, p_{T}^{j})/(p_{T}^{i} + p_{T}^{j});z'
        ]
else :
    hists = ['h2_htAK8', 'h2_ptAK8', 'h2_yAK8', 'h2_mAK8', 'h2_msoftdropAK8', 'h2_rho_all']
    titles = [
        'AK8 H_{T};H_{T} (GeV)',
        'AK8 p_{T};p_{T} (GeV)',
        'AK8 Rapidity;y',
        'AK8 ungroomed mass;Mass (GeV)',
        'AK8 soft-drop mass, z_{cut}=0.1, #beta=0;Mass (GeV)',
        'AK8 Jet #rho = (m/p_{T}R)^{2};#rho',
        #'AK8 #tau_{21} = #tau_{2} / #tau_{1};#tau_{21}',
        #'AK8 #Delta R between subjets;#Delta R',
        #'AK8 Jet Fragmentation z = min(p_{T}^{i}, p_{T}^{j})/(p_{T}^{i} + p_{T}^{j});z'
        ]
stacks = []
canvs = []
legs = []

ROOT.gStyle.SetPadRightMargin(0.15)

for ihist,histname in enumerate(hists):
    stack = ROOT.THStack(histname + '_stack', titles[ihist])
    canv = ROOT.TCanvas(histname + '_canv', histname +'_canv')
    leg = ROOT.TLegend(0.86, 0.3, 1.0, 0.8)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)    
    for itrig,trigname in enumerate(trigs) :
        s = histname + '_' + trigname
        print 'Getting ' + s
        hist = f.Get( s )
        if ihist == 0 : 
            hist.SetLineColor( colors1[itrig] )
            hist.SetMarkerStyle(1)
        else :
            hist.SetFillColor( colors2[itrig] )
        hist.Sumw2()
        
        if options.rebin != None :
            hist.Rebin( options.rebin )
        hist.Scale( scales[itrig] )
        stack.Add( hist )
        if ihist == 0 : 
            leg.AddEntry( hist, trigname, 'l')
        else :
            leg.AddEntry( hist, trigname, 'f')
    if ihist == 0 :
        stack.Draw('ehist nostack')
    else :
        stack.Draw("hist")
    if logy[ihist] : 
        canv.SetLogy()
        stack.SetMinimum(0.1)
    leg.Draw()
    canv.Update()
    canvs.append(canv)
    stacks.append(stack)
    legs.append(leg)
    canv.Print( 'exovv_trigplots_' + options.outname + '_' + histname + '.png', 'png')
    canv.Print( 'exovv_trigplots_' + options.outname + '_' + histname + '.pdf', 'pdf')
