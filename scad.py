import copy
import opsc
import oobb
import oobb_base

#notes
## tray depth is depth minus a clearance_bottom

clearance_tray_edges = 0 #clearance for each tray
clearance_tray_main = 1 #clearance for an entire tray
clearance_bottom = 2 # thickness of the bottom of the tray
clearance_bottom_tray = clearance_bottom
clearance_wall = 3 #thickness of the walls
clearance_wall_tray = 1 #thickness of the walls
clearance_lid = 2

depth_lid_overhang = 3

gap_between_lid_and_wall = 0.75
thickness_lid_wall_exterior = 1.5



###### old variables

clearance_design = 1
cd = clearance_design





width_hinge = 20
width_hinge_inside = width_hinge - 10

diameter_latch_inside = 15 - 6 - clearance_wall
extra_latch_side = 5
width_latch_inside = 5
width_latch_knob = 5
els = extra_latch_side

extra_for_30_mm_bolt_clearance = 12


width_latch = els + width_latch_inside + cd + els + width_latch_knob + cd + els + width_latch_inside + cd + extra_for_30_mm_bolt_clearance

diameter_hinge_inside = 15 - 2 - clearance_wall
diameter_hinge_bottom = 12
diameter_latch_bottom = 15
diameter_latch_knob = 11


extra_lid_overhang = thickness_lid_wall_exterior + gap_between_lid_and_wall



def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    run_fast = False
    run_fast_fast = False

    run_fast = True
    #run_fast_fast = True
    
    # save_type variables
    if True:
        filter = ""
        #filter = "main_body"
        #filter = "hinge"
        #filter = "lid"
        #filter = "latch"
        #filter = "latch_knob"

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 12
        kwargs["height"] = 12
        kwargs["thickness"] = 6

    # project_variables
    if True:
        pass
    
    # declare parts
    
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_bolt_packaging_three_d_printed_version_1" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        # trays
        if True:    
            tray_sizes = []
            if run_fast:
                tray_sizes.append({"width": 2.5, "height": 2})
                tray_sizes.append({"width": 5, "height": 4})
                tray_sizes.append({"width": 5, "height": 2})
                tray_sizes.append({"width": 4, "height": 2.5})
                tray_sizes.append({"width": 4, "height": 1})
                tray_sizes.append({"width": 3, "height": 3})
                tray_sizes.append({"width": 3, "height": 2})
                tray_sizes.append({"width": 4, "height": 2})
                tray_sizes.append({"width": 4, "height": 3})
                tray_sizes.append({"width": 4, "height": 4})
            if run_fast_fast:
                tray_sizes.append({"width": 2, "height": 2})

            
            thicknesses = [12,18,21,24]

            sizes_complete = []
            for size in tray_sizes:            
                    for thickness in thicknesses:
                        sizes_complete.append({"width": size["width"], "height": size["height"], "thickness": thickness})

            for size in sizes_complete:
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                #p3["thickness"] = 6
                part["kwargs"] = p3
                w = size["width"]
                h = size["height"]
                p3["width"] = w
                p3["height"] =  h
                #p3["extra"] = extra 
                p3["thickness"] = size["thickness"]
                part["name"] = "tray"
                parts.append(part)                

                             
                

        #main_bodies
        if True:
            main_body_widths = []
            main_body_heights = []

            thicknesses = []
        if run_fast:
            #main_body_widths = [9]
            #main_body_heights = [9]
            #thicknesses = [24]
            main_body_widths = [10]
            main_body_heights = [8]
            thicknesses = [18]
        if run_fast_fast:
            main_body_widths = [4]
            main_body_heights = [2]
            thicknesses = [12]

        for width in main_body_widths:
            for height in main_body_heights:
                for thickness in thicknesses:
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    part["kwargs"] = p3
                    w = width
                    h = height
                    p3["width"] = w
                    p3["height"] =  h
                    #p3["extra"] = extra 
                    p3["thickness"] = thickness
                    part["name"] = "main_body"
                    parts.append(part)
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                part["kwargs"] = p3
                w = width
                h = height
                p3["width"] = w
                p3["height"] =  h
                #p3["extra"] = extra 
                p3["thickness"] = 2
                part["name"] = "lid"
                parts.append(part)


        """
        for size in sizes_complete:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            #p3["thickness"] = 6
            part["kwargs"] = p3
            w = size["width"]
            h = size["height"]
            p3["width"] = w
            p3["height"] =  h
            width_tray = size["width_tray"]
            p3["width_tray"] = width_tray
            height_tray = size["height_tray"]
            p3["height_tray"] = height_tray
            extra = f"tray_size_{width_tray}_wide_{height_tray}_high"
            
            width_full = w * width_tray
            p3["width_full"] = width_full
            width_full_mm = width_full * 15            
            p3["width_full_mm"] = width_full_mm            
            height_full = h * height_tray
            p3["height_full"] = height_full
            height_full_mm = height_full * 15
            p3["height_full_mm"] = height_full_mm
                    
            #main body variables
            width_tray_tray = w * width_tray
            p3["width_tray_tray"] = width_tray_tray
            width_tray_tray_mm = width_tray_tray * 15
            p3["width_tray_tray_mm"] = width_tray_tray_mm
            height_tray_tray = h * height_tray
            p3["height_tray_tray"] = height_tray_tray
            height_tray_tray_mm = height_tray_tray * 15
            p3["height_tray_tray_mm"] = height_tray_tray_mm  
            global clearance_wall
            default_shift_hinge = width_tray_tray_mm / 2 - width_hinge/2 + clearance_wall/2
            p3["shift_hinge"] = default_shift_hinge

            p3["extra"] = extra 
            p3["thickness"] = size["thickness"]
            part["name"] = "main_body"
            parts.append(part)
            
            part = copy.deepcopy(part)
            p3 = copy.deepcopy(p3)
            width_full = w * width_tray + (2 * clearance_wall)/15
            p3["width_full"] = width_full
            width_full_mm = width_full * 15 + (2 * clearance_wall)            
            p3["width_full_mm"] = width_full_mm            
            height_full = h * height_tray + (2 * clearance_wall)/15
            p3["height_full"] = height_full
            height_full_mm = height_full * 15 + (2 * clearance_wall)
            p3["height_full_mm"] = height_full_mm
            
            part["kwargs"] = p3            
            part["name"] = "main_body_pots"
            parts.append(part)

            part = copy.deepcopy(part)
            part["name"] = "lid"
            part["kwargs"]["thickness"] = clearance_lid # depth_lid
            parts.append(part)

        """

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 15
        p3["width"] = 1
        p3["height"] = 2
        part["kwargs"] = p3
        part["name"] = "hinge"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p4 = copy.deepcopy(p3)
        p4["thickness"] = 20
        part["kwargs"] = p4
        part["name"] = "hinge"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 15
        p3["width"] = 1
        p3["height"] = 1
        part["kwargs"] = p3
        part["name"] = "latch"
        parts.append(part)
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 5
        p3["width"] = 1
        p3["height"] = 1
        part["kwargs"] = p3
        part["name"] = "latch_knob"
        parts.append(part)

        
        


        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


def get_hinge(thing, **kwargs):  

    #adding variables
    global clearance_design 
    global clearance_wall
    global width_hinge
    kwargs["width_hinge"] = width_hinge


    pos = kwargs.get("pos", [0, 0, 0])
    p3 = copy.deepcopy(kwargs)
    pos1 = copy.deepcopy(pos)
    #pos1[0] += 30
    p3["pos"] = pos1
    get_hinge_bottom(thing, **p3)
    
    
    p3 = copy.deepcopy(kwargs)
    pos1 = copy.deepcopy(pos)
    pos1[0] += 30
    p3["pos"] = pos1
    p3["depth_lid"] = 2
    get_hinge_top(thing, **p3)

def get_hinge_bottom(thing, **kwargs):
    
    depth = kwargs.get("thickness", 4)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)
    pos = kwargs.get("pos", [0, 0, 0])
    pos_plate = copy.deepcopy(pos)
    pos_plate[1] += -height * 15 / 4
    pos_plate[2] += -depth /2
    prepare_print = kwargs.get("prepare_print", False)
    radius_screw = kwargs.get("radius_screw", "m3")

    # variable
    global clearance_design
    screw_rotation = kwargs.get("screw_rotation", False)
    clearance_hinge_bottom = kwargs.get("clearance_hinge_bottom", True)
    
    
    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    global diameter_hinge_bottom
    p3["radius"] = diameter_hinge_bottom / 2
    global width_hinge
    d = width_hinge
    p3["depth"] = d
    p3["rot"] = [0, 90, 0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += -d/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add connecting cube top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_hinge
    h = height*15 - 7.5    
    d = depth
    if clearance_hinge_bottom:
        d += -depth_lid_overhang - clearance_design
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos_plate)
    pos1[1] += -7.5 /2   
    pos1[2] += (15 - depth)  /2    
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add connecting cube bottom
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_hinge
    h = height * 15 - (15 - diameter_hinge_bottom)
    d = depth - 15/2
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos_plate)
    pos1[1] += 0
    pos1[2] += (15 - depth)  /2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    
    extra_rear = 3
    #add cutout central
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cube"
    global width_hinge_inside
    w = width_hinge_inside + clearance_design
    global clearance_wall
    h = 15 - clearance_wall + extra_rear
    d = depth
    p3["zz"] = "middle"
    size = [w, h, d]
    p3["size"] = size 
    pos1 = copy.deepcopy(pos)
    pos1[1] += extra_rear/2
    pos1[2] += (15 - depth)  /2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    

    #add screw
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = radius_screw
    pos2 = copy.deepcopy(pos)
    pos2[0] += width_hinge / 2
    if screw_rotation:
        pos2[0] += -width_hinge
    p3["pos"] = pos2    
    p3["nut"] = True
    p3["depth"] = width_hinge
    if radius_screw == "m6":
        p3["depth"] += 3
    p3["rot"] = [0, 90, 0]
    if screw_rotation:
        p3["rot"] = [0, 270, 0]
    #p3["m"] = "#"
    p3["overhang"] = False
    oobb_base.append_full(thing,**p3)

    #add lid clearance
    clearance_hinge_bottom_old_style_cutout = False
    if clearance_hinge_bottom_old_style_cutout:
        #angled piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = width_hinge
        h = 12 #extra_lid_overhang + clearance_design
        d = 6 # depth_lid_overhang + clearance_design
        size = [w, h, d]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[1] += -0#-15/2 + extra_lid_overhang/2
        pos1[2] += 4.5#15/2
        p3["zz"] = "bottom"
        p3["rot"] = [22.5, 0, 0]
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
        # flat piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = width_hinge
        h = 3 #extra_lid_overhang + clearance_design
        d = 6 # depth_lid_overhang + clearance_design
        size = [w, h, d]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[1] += -5.75#-15/2 + extra_lid_overhang/2
        pos1[2] += 7.5#15/2
        p3["zz"] = "middle"
        #p3["rot"] = [22.5, 0, 0]
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_hinge_top(thing, **kwargs):
    
    
    depth = kwargs.get("thickness", 4)
    #depth not used always 15
    depth = 15
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)
    pos = kwargs.get("pos", [0, 0, 0])
    pos_plate = copy.deepcopy(pos)
    pos_plate[1] += -height * 15 / 4
    pos_plate[2] += -depth /2
    prepare_print = kwargs.get("prepare_print", False)
    width_hinge = kwargs.get("width_hinge", 5)

    radius_screw = kwargs.get("radius_screw", "m3")

    # variable
    clearance_design = kwargs.get("clearance_design", 0.5)
    depth_lid = kwargs.get("depth_lid", None)

    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"  
    global diameter_hinge_inside   
    radius_hinge_top = diameter_hinge_inside / 2
    p3["radius"] = radius_hinge_top
    d = width_hinge_inside
    p3["depth"] = d
    p3["rot"] = [0, 90, 0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += -d/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add cube to top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_hinge_inside
    r = diameter_hinge_inside
    h = r
    d = depth/2
    size = [w, h, d]
    p3["size"] = size    
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    pos1[1] += 0
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
      
    #add attachment
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_hinge_inside
    h = ((height-0.5)*15) + diameter_hinge_inside/2
    d = depth_lid
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    pos1[1] += -((height-0.5)*15) / 2 + diameter_hinge_inside/4
    pos1[2] += depth/2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    # add hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = radius_screw
    d = width_hinge_inside
    p3["depth"] = d
    p3["rot"] = [0, 90, 0]    
    pos1 =  copy.deepcopy(pos)
    pos1[0] += -d/2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

def get_latch(thing, **kwargs):  

    #adding variables
    global clearance_design
    kwargs["clearance_design"] = clearance_design
    global clearance_wall
    global width_hinge
    kwargs["width_hinge"] = width_hinge


    pos = kwargs.get("pos", [0, 0, 0])
    p3 = copy.deepcopy(kwargs)
    pos1 = copy.deepcopy(pos)
    pos1[0] += 135
    p3["pos"] = pos1
    p3["test"] = True
    get_latch_bottom(thing, **p3)
    
    
    p3 = copy.deepcopy(kwargs)
    pos1 = copy.deepcopy(pos)
    pos1[0] += 45
    p3["pos"] = pos1
    p3["depth_lid"] = 2
    get_latch_top(thing, **p3)
    
    p3 = copy.deepcopy(kwargs)
    pos1 = copy.deepcopy(pos)
    #pos1[0] += 90
    p3["pos"] = pos1
    
    get_latch_knob(thing, **p3)


def get_latch_bottom(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)
    pos = kwargs.get("pos", [0, 0, 0])
    pos_plate = copy.deepcopy(pos)
    pos_plate[1] += 0
    pos_plate[2] += -depth /2
    prepare_print = kwargs.get("prepare_print", False)
    radius_screw = kwargs.get("radius_screw", "m3")

    # variable
    global clearance_design
    screw_rotation = kwargs.get("screw_rotation", False)
    clearance_hinge_bottom = kwargs.get("clearance_hinge_bottom", True)
    test = kwargs.get("test", False)
    

    extra_connecting_cube_height = 3
    #add connecting cube rounded
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    
    w = width_latch
    h = 15 * height - extra_connecting_cube_height
    d = depth - depth_lid_overhang   
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos_plate)    
    extra_side = extra_latch_side
    pos1[0] += w/2 - extra_side - (width_latch_inside+clearance_design)/2 
    pos1[1] += -(h - 15)/2
    pos1[2] += (15 - depth)  /2    
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add connecting cube square bit
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_latch
    extra_test = 3
    radius_corner = 5
    h = h  - radius_corner
    if test:
        h += extra_test
    d = depth - depth_lid_overhang    
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos1)
    pos1[1] += radius_corner/2 + extra_test/2
    pos1[2] += 0
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    extra_rear = 3
    #add cutout central
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cube"
    w = width_latch_inside + clearance_design
    h = 15 - clearance_wall + extra_rear
    d = depth
    p3["zz"] = "middle"
    size = [w, h, d]
    p3["size"] = size 
    pos1 = copy.deepcopy(pos)
    pos1[1] += -extra_rear/2
    pos1[2] += (15 - depth)  /2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)


    #add cutout knob
    p3 = copy.deepcopy(p3)
    w = width_latch_knob + clearance_design
    h = h
    d = d
    size = [w, h, d]
    p3["size"] = size 
    pos1 = copy.deepcopy(pos1)
    pos1[0] +=  w + extra_side
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    
    

    #add screw
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = radius_screw
    pos2 = copy.deepcopy(pos)
    pos2[0] += 0 - (width_latch_inside + clearance_design)/ 2 - extra_latch_side
    p3["pos"] = pos2    
    p3["depth"] = width_latch
    p3["rot"] = [0, 90, 0]
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    
    #add nut
    p3 = copy.deepcopy(p3)
    p3["type"] = "n"
    p3["shape"] = f"oobb_nut"
    p3["radius_name"] = radius_screw
    p3["depth"] = 25
    pos2 = copy.deepcopy(pos)
    if True:
        extra_latch_side
        els = extra_latch_side
        cd = clearance_design

        shift_start = (width_latch_inside + cd)/ 2 + els
        shift = els + width_latch_inside + cd + els + width_latch_knob + cd 
        pos2[0] = -shift_start + shift
    #pos2[2] += 15    
    p3["pos"] = pos2
    p3["hole"] = False
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    # add lock bolt position viewing holes
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"
    d = 5
    p3["depth"] = d
    p3["rot"] = [0, 0, 0]
    if True:
        poss = []
        pos1 =  copy.deepcopy(pos)
        #for 3 mm bolt
        shift_closed = 10
        shift_middle = shift_closed + 5
        shift_open = shift_closed + 10
        pos1[0] += width_latch_inside/2 + clearance_design/2 + extra_latch_side + width_latch_knob + clearance_design
        pos11 = copy.deepcopy(pos1)
        pos11[0] += shift_closed
        pos12 = copy.deepcopy(pos1)
        pos12[0] += shift_middle
        pos13 = copy.deepcopy(pos1)
        pos13[0] += shift_open
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)    
    p3["pos"] = poss
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    

def get_latch_top(thing, **kwargs):       
    
    depth = kwargs.get("thickness", 4)
    #depth not used always 15
    depth = 15
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)
    pos = kwargs.get("pos", [0, 0, 0])
    pos_plate = copy.deepcopy(pos)
    pos_plate[1] += -height * 15 / 4
    pos_plate[2] += -depth /2
    prepare_print = kwargs.get("prepare_print", False)
    width_hinge = kwargs.get("width_hinge", 5)

    radius_screw = kwargs.get("radius_screw", "m3")

    # variable
    clearance_design = kwargs.get("clearance_design", 0.5)
    depth_lid = kwargs.get("depth_lid", None)

    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"  
    global diameter_hinge_inside   
    radius_hinge_top = diameter_latch_inside / 2
    p3["radius"] = radius_hinge_top
    d = width_latch_inside
    p3["depth"] = d
    p3["rot"] = [0, 90, 0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += -d/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add cube to top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_latch_inside
    r = diameter_latch_inside
    h = r
    d = depth/2
    size = [w, h, d]
    p3["size"] = size    
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    pos1[1] += 0
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
      
    #add attachment
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cube"
    w = width_latch_inside
    h = diameter_latch_inside + extra_lid_overhang + height * 15
    d = depth_lid + depth_lid_overhang
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    pos1[1] += extra_lid_overhang/2 + (height * 15) / 2
    pos1[2] += depth/2 - depth_lid_overhang
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    # add hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = radius_screw
    d = width_hinge_inside
    p3["depth"] = d
    p3["rot"] = [0, 90, 0]    
    pos1 =  copy.deepcopy(pos)
    pos1[0] += -d/2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    

def get_latch_knob(thing, **kwargs):

    pos = kwargs.get("pos", [0, 0, 0])

    #main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = diameter_latch_knob / 2
    p3["depth"] = width_latch_knob
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #nut
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_nut"
    p3["radius_name"] = "m3"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    p3["hole"] = True
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add knurling
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cube_new"
    w = 3
    h = 3
    d = width_latch_knob
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    pos1[1] += 0
    pos1[2] += 0
    p3["zz"] = "middle"
    p3["pos"] = pos1
    #p3["m"] = "#"
    p3["rot"] = [0, 0, 45]
    rot_shifts = []
    num_notches = 32
    extra_shift = 1.5
    for x in range(0, num_notches+1):
        angle = 360/num_notches * x
        rot_shifts.append([[diameter_latch_knob/2+extra_shift,0,0],[0,0,angle]])
    p3["rot_shift"] = rot_shifts
    oobb_base.append_full(thing,**p3)



def get_lid(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    height = kwargs.get("height", 10)
    width = kwargs.get("width", 10)

    # main body
    p3 = copy.deepcopy(kwargs)    
    pos = p3.get("pos", [0, 0, 0])
    pos1 = copy.deepcopy(pos)    
    p3["pos"] = pos1
    get_lid_basic(thing, **p3)
    

    #hinge variables
    #adding variables

    #hinge
    
    shift_hinge = width * 15 / 2 - width_hinge/2 + clearance_wall + clearance_tray_main/2

    p3 = copy.deepcopy(kwargs)    
    p3["thickness"] = depth + clearance_bottom
    p3["width"] = 1
    p3["height"] = 2
    poss = []
    pos1 = copy.deepcopy(pos)
    pos1[1] += get_variable("shift_hinge_y", height=height)
    pos1[2] += -7.5
    pos11 = copy.deepcopy(pos1)
    pos11[0] += shift_hinge
    pos12 = copy.deepcopy(pos1)
    pos12[0] += -shift_hinge
    poss.append(pos11)
    poss.append(pos12)
    screw_rotation = False
    for pos1 in poss:
        p4 = copy.deepcopy(p3)
        p4["screw_rotation"] = screw_rotation
        p4["pos"] = pos1
        p4["depth_lid"] = depth
        get_hinge_top(thing, **p4)
        screw_rotation = not screw_rotation

    #add latch
    p3 = copy.deepcopy(kwargs)
    p3["thickness"] =  depth + clearance_bottom
    p3["width"] = 1
    p3["height"] = 2
    poss = []    
    if True:
        pos1 = copy.deepcopy(pos)
        pos1[1] += -get_variable("shift_hinge_y", height=height)
        pos1[2] += -7.5
        p3["pos"] = pos1
    p3["depth_lid"] = depth
    get_latch_top(thing, **p3)

def get_lid_basic(thing, **kwargs):
    thickness = kwargs.get("thickness", 4)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)    
    pos = kwargs.get("pos", [0, 0, 0])

    #main piece
    extra_size = (clearance_wall * 2 
                 + clearance_tray_main 
                 + gap_between_lid_and_wall * 2 
                 + thickness_lid_wall_exterior * 2)
    width_full = (width * 15 
                 + extra_size)
    height_full = (height * 15 
                    + extra_size )

    depth = thickness + depth_lid_overhang

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    w = width_full
    h = height_full
    d = thickness
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    rad = (5            
           + clearance_wall 
           + clearance_tray_main / 2 
           + gap_between_lid_and_wall  
           + thickness_lid_wall_exterior)
    p3["radius"] = rad
    oobb_base.append_full(thing,**p3)
    
    
    #interior hollow
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"    
    p3["shape"] = f"oobb_rounded_rectangle_hollow"
    #p3["shape"] = f"rounded_rectangle"
    w = width_full
    h = height_full
    d = depth_lid_overhang
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    pos1[2] += -depth_lid_overhang
    p3["pos"] = pos1
    p3["radius"] = rad
    p3["wall_thickness"] = thickness_lid_wall_exterior
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    
    p4 = copy.deepcopy(p3)
    p4["type"] = "negative"
    p4["extra"] = "interior"
    size = p4["size"]
    extra_up = 5
    size[2] += extra_up
    pos1 = p4["pos"]
    pos1[2] -= extra_up
    #p4["m"] = "#"
    oobb_base.append_full(thing,**p4)
    



def get_main_body(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    height = kwargs.get("height", 10)
    width = kwargs.get("width", 10)

    # main body
    p3 = copy.deepcopy(kwargs)    
    pos = p3.get("pos", [0, 0, 0])
    pos1 = copy.deepcopy(pos)    
    p3["pos"] = pos1
    get_main_body_basic(thing, **p3)
    

    #hinge variables
    #adding variables

    #hinge
    
    shift_hinge = width * 15 / 2 - width_hinge/2 + clearance_wall + clearance_tray_main/2

    p3 = copy.deepcopy(kwargs)    
    p3["thickness"] = depth + clearance_bottom
    p3["width"] = 1
    p3["height"] = 2
    poss = []
    pos1 = copy.deepcopy(pos)
    pos1[1] += get_variable("shift_hinge_y", height=height)
    pos1[2] += depth + clearance_bottom - 7.5
    pos11 = copy.deepcopy(pos1)
    pos11[0] += shift_hinge
    pos12 = copy.deepcopy(pos1)
    pos12[0] += -shift_hinge
    poss.append(pos11)
    poss.append(pos12)
    screw_rotation = False
    for pos1 in poss:
        p4 = copy.deepcopy(p3)
        p4["screw_rotation"] = screw_rotation
        p4["pos"] = pos1
        get_hinge_bottom(thing, **p4)
        screw_rotation = not screw_rotation

    #add latch
    p3 = copy.deepcopy(kwargs)
    p3["thickness"] =  depth + clearance_bottom
    p3["width"] = 1
    p3["height"] = 1
    poss = []    
    if True:
        pos1 = copy.deepcopy(pos)
        pos1[1] += -get_variable("shift_hinge_y", height=height)
        pos1[2] += depth + clearance_bottom - 7.5
        p3["pos"] = pos1
    get_latch_bottom(thing, **p3)

def get_main_body_basic(thing, **kwargs):
    thickness = kwargs.get("thickness", 4)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)    
    pos = kwargs.get("pos", [0, 0, 0])

    #main piece
    width_full = width * 15 + clearance_wall * 2 + clearance_tray_main
    height_full = height * 15 + clearance_wall * 2 + clearance_tray_main

    depth = thickness + clearance_bottom

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    w = width_full
    h = height_full
    d = depth
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    p3["radius"] = 5 + clearance_wall + clearance_tray_main / 2
    oobb_base.append_full(thing,**p3)
    
    #interior hollow
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"rounded_rectangle"
    w = width_full - clearance_wall * 2
    h = height_full - clearance_wall * 2
    d = thickness
    size = [w, h, d]
    p3["size"] = size
    pos1 = copy.deepcopy(pos)
    pos1[2] += clearance_bottom
    p3["pos"] = pos1
    p3["radius"] = 5 + clearance_tray_main / 2
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)
    



def get_tray(thing, **kwargs):
    thickness = kwargs.get("thickness", 4)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 10)    
    pos = kwargs.get("pos", [0, 0, 0])

    depth = thickness

    #main block
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    
    w = width * 15
    h = height * 15 
    d = depth
    size = [w, h, d]
    p3["size"] = size
    p3["radius"] = 5
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #hollow out tray
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"rounded_rectangle"
    w = width * 15 - clearance_wall_tray * 2
    h = height * 15 - clearance_wall_tray * 2
    d = depth - clearance_bottom_tray
    size = [w, h, d]
    p3["size"] = size
    p3["radius"] = 5 - clearance_wall_tray
    pos1 = copy.deepcopy(pos)
    pos1[2] += clearance_bottom_tray
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

        

###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]
    func(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    

def get_variable(name,height=None):
    if name == "shift_hinge_y":
        return height * 15 / 2 + clearance_wall + 7.5  




if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)