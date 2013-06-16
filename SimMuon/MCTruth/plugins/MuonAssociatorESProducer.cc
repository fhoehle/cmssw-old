#include <memory>
#include "boost/shared_ptr.hpp"

#include "FWCore/Framework/interface/ESProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ModuleFactory.h"

#include "SimMuon/MCTruth/interface/MuonAssociatorByHits.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"

class MuonAssociatorESProducer : public edm::ESProducer
{
public:

    MuonAssociatorESProducer(edm::ParameterSet const & config) : config_(config)
    {
        setWhatProduced(this, config.getParameter<std::string>("ComponentName"));
    }

    ~MuonAssociatorESProducer() {}

    typedef boost::shared_ptr<TrackAssociatorBase> ReturnType;

    ReturnType produce(const TrackAssociatorRecord & record)
    {
        using namespace edm::es;
        boost::shared_ptr<TrackAssociatorBase> pMuonAssociatorByHits( new MuonAssociatorByHits(config_) );
        return pMuonAssociatorByHits;
    }

private:

    edm::ParameterSet config_;
};

DEFINE_FWK_EVENTSETUP_MODULE(MuonAssociatorESProducer);
