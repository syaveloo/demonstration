if (SERVER) then
    AddCSLuaFile("weaponfov.lua")

end

if (CLIENT) then

    fov = 54

    CreateClientConVar( "globalfov", 0, false, false)
    function FovUpdate( ply, key )
        if (GetConVar( "globalfov" ):GetInt() == 1) then
            if (key== IN_USE) then
                for _,w in ipairs(LocalPlayer():GetWeapons()) do
                    w.ViewModelFOV = fov
                end
            end
        end
    end
    hook.Add( "KeyPress", "fovupdate", FovUpdate )

    hook.Add( "PopulateToolMenu", "WeaponMenuSettings", function()
        spawnmenu.AddToolMenuOption( "Utilities", "weaponFov", "WeaponFov_Menu", "#WeaponFov", "", "", function( panel )
            panel:AddControl( "Slider", { Label = "#weaponfov_wb", Type = "Integer", Command = "weaponfov_wb", Min = 50, Max = 150 } )
            panel:ControlHelp( "'Weapon Base' based weapons" ):DockMargin( 16, 4, 16, 16 )
            
            panel:AddControl( "CheckBox", { Label = "E to return fov", Command = "globalfov" } )
            panel:ControlHelp( "If checked: Press E to apply your fov to all weapons you have (Weapon Base).\n" .. "If NOT checked: Doesn`t save after death, but you can customize every weapon`s fov." ):DockMargin( 16, 4, 16, 16 )

            panel:AddControl( "Slider", { Label = "#weaponfov_tfa", Type = "Integer", Command = "weaponfov_tfa", Min = 0, Max = 50 } )
            panel:ControlHelp( "'TFA' based weapons" ):DockMargin( 16, 4, 16, 16 )

            panel:AddControl( "Slider", { Label = "#weaponfov_hl2", Type = "Integer", Command = "viewmodel_fov", Min = 54, Max = 150 } )
            panel:ControlHelp( "'HL2' based weapons" ):DockMargin( 16, 4, 16, 16 )
        end )
    end )
    hook.Add( "AddToolMenuCategories", "WeaponFovCategory", function()
        spawnmenu.AddToolCategory( "Utilities", "weaponFov", "#Weapon Fov" )
    end )

    concommand.Add( "weaponfov_wb", function( ply, cmd, args, argStr )
        fov = tonumber(args[1])
        LocalPlayer():GetActiveWeapon().ViewModelFOV = fov
    end, nil, "Weapon Base based weapons. change fov")
	
	concommand.Add( "weaponfov_tfa", function( ply, cmd, args, argStr)
		LocalPlayer():ConCommand( "cl_tfa_viewmodel_multiplier_fov " .. tonumber(args[1]) )
	end, nil, "TFA based weapons. change fov")
end