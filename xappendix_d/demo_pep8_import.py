# coding = utf8

"""
ʹ�õ������import��Ҫ��ѭ�Ĺ淶��
1������Ӧ����ģ��Ķ�����������ģ��ע��֮����ȫ�ֱ����ͳ�������֮ǰ��
2�������˳��Ӧ���ǣ���׼�⡢�������⡢����Ӧ�ÿ⡣
3��ÿ��importֻ����һ��ģ���������һ�����е������ģ������
4���ᳫʹ�þ��Ե���,��������ģ�����룺import *��
5���κ�ģ�����Ա�������__version__��__all__��__author__�ȣ�Ҫ���ڵ���֮ǰ��
   ���ǣ����from __future__ import ...�������ģ������д���֮ǰ��������ģ��ע��֮��


This is the example module.
This module show some formats.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'
MAX_NUM = 10000

import os
import sys
