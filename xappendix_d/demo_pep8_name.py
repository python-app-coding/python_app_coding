# coding = utf8


def demo_name_var():
    # ����ʹ��Ӣ�ĵ��ʺ����ֻ�ϵ������������������֮�����»������ӣ���ʹ�����ֿ�ʼ��
    # �Ե��»��߽����ı�������Ҫ����������Python�Ĺؼ��ֻ��׼��ʹ�õ����ơ�
    # �Ե��»��߿�ʼ�ı�����Ϊ�ڲ���������ʹ�á�import *�������ᵼ����Щ������
    student_count = 100
    math_ = True
    _module_sign = '01021330'


def demo_name_class_var():
    # �����ڲ�ʹ��˫�»��߿�ʼ�������Ի򷽷�����Ϊ�ڲ�ʹ�ö���
    # ���ⲿ����ʱ�ܵ�����������ֱ��ʹ�ñ������ã�����롰_��������Ϊǰ׺��

    class Student:
        __name = 'name'

    st = Student()
    print([p for p in dir(st) if '__name' in p])
    # ['_Student__name']


def demo_name_constant():
    # ����ͨ����ģ�鼶���壬���»������ӵĴ�д��ĸ��ʽ��ʾ������ģ��Ķ������������֮��
    import pkgutil
    from importlib import import_module

    DEFAULT_DB_ALIAS = 'default'
    DJANGO_VERSION_PICKLE_KEY = '_django_version'


def demo_class_name():
    # ������ʹ��CapWords��ʽ�����������ֱ�����ӣ�ÿ����������ĸ��д��

    class InterfaceError(Exception):
        pass


def demo_name_function():
    # �������������������Լ��������ͬ��ʹ��Сд��ʽ���������֮��ʹ���»������ӡ�

    def pretty_name(name):
        """Convert 'first_name' to 'First name'."""
        if not name:
            return ''
        return name.replace('_', ' ').capitalize()


def demo_name_parameter():
    # ���󷽷��еĵ�һ������ʹ��self����ʾ�������Ķ����෽���еĵ�һ������ʹ��cls����ʾ�౾��

    class Student:
        """ѧ����Ϣģ��"""
        school_name = "Ming Hu"

        def __init__(self):
            self.name = ''

        @classmethod
        def get_school_name(cls):
            return cls.school_name


if __name__ == '__main__':
    pass
