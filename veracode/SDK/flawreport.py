from veracode.SDK.core import Base

class GenerateFlawReport(Base):
    """ class: veracode.SDK.flawreport.GenerateFlawReport
    
        params: 
			app_id_list: required
			scan_type: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				app_id_list,
				scan_type=None,
        ):
        
        super(GenerateFlawReport, self).__init__(
            module='flawreport',
            cls='GenerateFlawReport',
            fn='get', 
            args={
				'app_id_list':app_id_list,
				'scan_type':scan_type,
            })
    