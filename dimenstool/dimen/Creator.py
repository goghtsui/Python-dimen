#!/usr/bin/env python

import io
from dimenstool.dimen import Type
import xml.dom.minidom as dom
from dimenstool.dimen import Switcher


class Creator:
    """  根据用户设置的 density  scale_density  xdpi  生成转换后的xml文件"""

    def __init__(self, density, scale_density, xdpi):
        """  初始化density  scale_density  xdpi  """
        # 在内存中创建一个空的文档
        self.doc = dom.Document()
        if density:
            self.density = density
        else:
            self.density = 1

        if scale_density:
            self.scale_density = scale_density
        else:
            self.scale_density = 1

        if xdpi:
            self.xdpi = xdpi
        else:
            self.xdpi = 160

    def create_root(self):
        """ 定义根节点  resources"""
        # 创建一个根节点对象
        root = self.create_element(Type.resources)
        # 将根节点添加到文档对象中
        self.doc.appendChild(root)
        return root

    def create_element(self, element_name, node_tag=None, node_name=None, node_vlaue=None):
        """  生成一个节点对象，并添加属性值及文本内容  """
        # 创建一个节点对象
        root = self.doc.createElement(element_name)

        # 设置节点的属性
        if node_tag and node_name:
            root.setAttribute(node_tag, node_name)

        # 给节点添加一个文本节点
        if node_vlaue:
            root.appendChild(self.doc.createTextNode(
                str(Switcher.format_value(node_vlaue, self.density, self.scale_density, self.xdpi))))

        return root

    def creat_xml(self, node_tree_list):
        """  将解析的xml数据，重新生成一个新的xml文件  """
        root = self.create_root()
        if node_tree_list is not None:
            for node in node_tree_list:
                for (key, value) in node.items():
                    node_item = self.create_element(Type.dimen, Type.name, key, value)
                    root.appendChild(node_item)

        return root

    def parse_string(self, content):
        return dom.parseString(content)

    def get_child_notes(self):
        writer = io.StringIO()
        self.doc.writexml(writer, addindent="\r\n", newl='\r\n', encoding="utf-8")
        return writer.getvalue()
