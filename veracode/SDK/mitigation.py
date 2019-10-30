from veracode.SDK.core import Base

class GetMinigationInfo(Base):
    """ class: veracode.SDK.mitigation.GetMinigationInfo
    
        params: 
			flaw_id_list: required
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				flaw_id_list,
				build_id,
        ):
        
        super(GetMinigationInfo, self).__init__(
            module='mitigation',
            cls='GetMinigationInfo',
            fn='get', 
            args={
				'flaw_id_list':flaw_id_list,
				'build_id':build_id,
            })
    