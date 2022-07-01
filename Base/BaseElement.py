from Base.BaseCommon import BaseCommon


def element(tag_name, var_name):
    return BaseCommon()._get_element_ini(tag_name, var_name)


if __name__ == '__main__':
    print(element('MainActivity', 'Connect_Button'))
