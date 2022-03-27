if (SERVER) then
    AddCSLuaFile("weaponfov.lua")
    
    function GlowPlayers(ply, cmd, args)
        plys = player.GetAll()
        PrintTable(plys)
    end
    concommand.Add( "glowplayers", GlowPlayers, nil,"",0)

end

if (CLIENT) then

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
            panel:AddControl( "Slider", { Label = "#weaponfov", Type = "Integer", Command = "weaponfov", Min = 50, Max = 150 } )
            panel:ControlHelp( "Fov for weapons from addons" ):DockMargin( 16, 4, 16, 16 )
            
            panel:AddControl( "Slider", { Label = "weaponfov_internal", Type = "Integer", Command = "viewmodel_fov", Min = 54, Max = 150 } )
            panel:ControlHelp( "Fov for weapons from gmod (HALF-LIFE 2)" ):DockMargin( 16, 4, 16, 16 )
            
            panel:AddControl( "CheckBox", { Label = "WeaponFov for all weapons", Command = "glowplayers" } )
            panel:ControlHelp( "" ):DockMargin( 16, 4, 16, 16 )
        end )
    end )
    hook.Add( "AddToolMenuCategories", "WeaponFovCategory", function()
        spawnmenu.AddToolCategory( "Utilities", "weaponFov", "#Weapon Fov" )
    end )

    concommand.Add( "weaponfov", function( ply, cmd, args, argStr )
        fov = tonumber(args[1])
        LocalPlayer():GetActiveWeapon().ViewModelFOV = fov
    end, nil, "weaponfov <fov>")

    CreateClientConVar( "globalfov", 0, false, false)
    CreateClientConVar( "weaponfov_tfamode", 0, false, false)

end