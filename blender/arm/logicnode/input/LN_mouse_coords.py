from arm.logicnode.arm_nodes import *

class MouseCoordsNode(ArmLogicTreeNode):
    """Mouse coords node"""
    bl_idname = 'LNMouseCoordsNode'
    bl_label = 'Mouse Coords'
    arm_version = 1

    def init(self, context):
        super(MouseCoordsNode, self).init(context)
        self.add_output('NodeSocketVector', 'Coords')
        self.add_output('NodeSocketVector', 'Movement')
        self.add_output('NodeSocketInt', 'Wheel')

add_node(MouseCoordsNode, category=PKG_AS_CATEGORY, section='mouse')