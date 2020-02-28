import xlrd
import nnlog
import traceback
from config.setting import func_map,log

class ParamDeal:
    def read_excel(self,file_path):
        case_list = [] #存放所有的测试用例
        try:
            book = xlrd.open_workbook(file_path)
            sheet = book.sheet_by_index(0)
            for row in range(1,sheet.nrows):
                line = sheet.row_values(row)[1:7]
                line[2] = self.str_to_dict(self.replace_param(line[2]))#这个把请求参数转成字典
                line[3] = self.str_to_dict(self.replace_param(line[3])) #这个是把请求头也转成字典
                case_list.append(line)
        except Exception as e:
            log.error("读取用例文件出错，文件名是:%s"%file_path)
            log.error("具体的错误信息是%s"%traceback.format_exc())

        return case_list

    def replace_param(self,s):#替换参数化的
        for func_name, func in func_map.items():
            if func_name in s:
                result = func()
                s = s.replace(func_name, result)
        return s

    def str_to_dict(self,s):#把请求参数的字符串转成字典
        d = {}
        if s.strip():#为了判断参数是否为空
            for t in s.split(','):
                k, v = t.split('=')
                d[k] = v
        return d

if __name__ == '__main__':
    p = ParamDeal()
    result = p.read_excel('/Users/nhy/PycharmProjects/cnz/day9/atp/config/用例模板.xlsx')
    print(result)


