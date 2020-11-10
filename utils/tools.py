from bl_ui.space_toolsystem_toolbar import VIEW3D_PT_tools_active as view3d_tools


def get_tools_from_context(context):
    tools = {}

    active = view3d_tools.tool_active_from_context(context)

    for tool in view3d_tools.tools_from_context(context):
        if tool:

            # tuple tool
            if type(tool) is tuple:
                for subtool in tool:
                    tools[subtool.idname] = {'label': subtool.label,
                                             'icon_value': view3d_tools._icon_value_from_icon_handle(subtool.icon),
                                             'active': subtool.idname == active.idname}

            # single tool
            else:
                tools[tool.idname] = {'label': tool.label,
                                      'icon_value': view3d_tools._icon_value_from_icon_handle(tool.icon),
                                      'active': tool.idname == active.idname}

    return tools


def get_active_tool(context):
    tools = get_tools_from_context(context)

    for idname, tooldict in tools.items():
        if tooldict['active']:
            return idname


def get_tool_options(context, tool_idname, operator_idname):
    for tooldef in context.workspace.tools:
        if tooldef and tooldef.idname == tool_idname:
            if tooldef.mode == context.mode:
                try:
                    return tooldef.operator_properties(operator_idname)
                except:
                    return None
