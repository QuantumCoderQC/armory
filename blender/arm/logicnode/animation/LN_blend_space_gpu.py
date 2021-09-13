from arm.logicnode.arm_advanced_draw import *
from arm.logicnode.arm_nodes import *
from bpy.props import *
from bpy.types import Node

class BlendSpaceNode(ArmLogicTreeNode):
    """Activates the output when the given event is received.

    @seeNode Send Event to Object
    @seeNode Send Event"""
    bl_idname = 'LNBlendSpace'
    bl_label = 'Blend Space'
    arm_version = 1
    arm_section = 'custom'

    my_bool: BoolProperty(
        name="Enable or Disable",
        description="A bool property",
        default = False
    )

    draw_handler_dict = {}

    def __init__(self):
        array_nodes[str(id(self))] = self
    
    def create_blend_space(self):
        self.blend_space = BlendSpaceGUI(self)
    
    def draw_advanced(self):
        if bpy.context.space_data.edit_tree == self.get_tree():
            self.blend_space.calculateBoundaries()
            self.blend_space.draw()

    def arm_init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')

    def add_advanced_draw(self):
        print('Adding')
        print(str(self.as_pointer()))
        handler = self.draw_handler_dict.get(str(self.as_pointer()))
        if handler is None:
            self.create_blend_space()
            editor = getattr(bpy.types, 'SpaceNodeEditor')
            handler = editor.draw_handler_add(self.draw_advanced, (), 'WINDOW', 'POST_VIEW')
            self.draw_handler_dict[str(self.as_pointer())] = handler
            print(self.draw_handler_dict)

    def remove_advanced_draw(self):
        print('Removing')
        print(str(self.as_pointer()))
        print(self.draw_handler_dict)
        handler = self.draw_handler_dict.get(str(self.as_pointer()))
        if handler is not None:
            print('Handler existing')
            editor = getattr(bpy.types, 'SpaceNodeEditor')
            editor.draw_handler_remove(handler, 'WINDOW')
            self.draw_handler_dict.pop(str(self.as_pointer()))

        
    def draw_buttons(self, context, layout):
        layout.prop(self, 'my_bool')
        op = layout.operator('arm.node_call_func', text='Show', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.callback_name = 'add_advanced_draw'
        op = layout.operator('arm.node_call_func', text='Hide', icon='X', emboss=True)
        op.node_index = str(id(self))
        op.callback_name = 'remove_advanced_draw'