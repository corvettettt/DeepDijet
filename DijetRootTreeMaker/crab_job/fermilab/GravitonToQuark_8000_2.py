from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = '/uscms_data/d3/zwang2/WorkingArea4/CMSSW_8_0_25/src/CMSDIJET/DijetRootTreeMaker/crab_job/output/'
config.General.requestName = 'GravitonToQuark_8000_2_fermi'

config.JobType.psetName = '/uscms_data/d3/zwang2/WorkingArea4/CMSSW_8_0_25/src/CMSDIJET/DijetRootTreeMaker/prod/flat-MC-cfg_miniAOD.py'
config.JobType.pluginName = 'Analysis'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt'
#config.JobType.outputFiles = 'Qstar_25ns_500.root'


config.Data.inputDataset = 'global'
config.Data.inputDataset = '/RSGravitonToQuarkQuark_kMpl01_M_8000_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM' 
config.Data.unitsPerJob = 1 #without '' since it must be an int
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Data.outputDatasetTag = 'analysis'
#config.Data.lumiMask = 'json_DCSONLY.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_254833_13TeV_PromptReco_Collisions15_JSON.txt'
#config.Data.lumiMask = 'lumis_all_sub_runb.json' #if you downloaded the file in the working directory
#config.Data.runRange = '296642-296643'#'208306-238354' # '193093-194075'                             
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/store/user/santanas/rootTrees/Run2015B_JetHT_10June2015DCSJson_JECV5_5a70fc3/'
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
config.Site.blacklist = []
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_IT_Rome'
