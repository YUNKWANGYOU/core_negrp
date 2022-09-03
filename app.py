import ErrPointHandler
import sys

if __name__=="__main__" :
    e = ErrPointHandler.ErrPointHandler()
    e.print_sheets()
    ip_route = e.df[e.sheet[3]]
    e.print_columns(ip_route)
    
    sys.stdout.write('\n\n')
    e.put_err_route()
    e.print_err_route()
    e.err_ip_mapping(ip_route)
    
    sys.stdout.write('\n')
    e.cal_point()
    e.save_cal_point()