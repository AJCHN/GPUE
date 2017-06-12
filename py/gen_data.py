#-------------gen_data.py------------------------------------------------------##
# Purpose: This file will take the data from GPUE and turn it into a bvox file
#          for visualization with blender
#
#------------------------------------------------------------------------------#

import numpy as np

xDim = yDim = zDim = 256

# Function to create plot with vtk
def to_vtk(item, xDim, yDim, zDim, nframes, filename):
    outfile = open(filename, "w")
    outfile.write("# vtk DataFile Version 3.0\n")
    outfile.write("vtkfile\n")
    outfile.write("ASCII\n")
    outfile.write("DATASET STRUCTURED_POINTS\n")
    outfile.write("DIMENSIONS "+str(xDim)+" "+str(yDim)+" "+str(zDim)+"\n")
    outfile.write("ORIGIN 0 0 0\n")
    outfile.write("SPACING 1 1 1\n")
    outfile.write("POINT_DATA " + str(xDim*yDim*zDim) + "\n")
    outfile.write("SCALARS scalars float 1\n")
    outfile.write("LOOKUP_TABLE default\n")
    for i in range(xDim):
        for j in range(yDim):
            for k in range(zDim):
                outfile.write(str(item[i][j][k]) + " ")
            outfile.write('\n')
        outfile.write('\n') 

# Function to plot wfc with pltvar as a variable to modify the type of plot
def wfc_density(xDim, yDim, zDim, data_dir, pltval, i):
    print(i)
    data_real = "../" + data_dir + "/wfc_0_const_%s" % i
    data_im = "../" + data_dir + "/wfc_0_consti_%s" % i
    if (pltval == "wfc_ev"):
        data_real = "../" + data_dir + "/wfc_ev_%s" % i
        data_im = "../" + data_dir + "/wfc_evi_%s" % i
    elif (pltval == "wfc_ramp"):
        data_real = "../" + data_dir + "/wfc_0_ramp_%s" % i
        data_im = "../" + data_dir + "/wfc_0_rampi_%s" % i
    lines_real = np.loadtxt(data_real)
    lines_im = np.loadtxt(data_im)
    print(len(lines_real))
    wfc_real = np.reshape(lines_real, (xDim,yDim,zDim));
    wfc_im = np.reshape(lines_im, (xDim,yDim, zDim));
    wfc = abs(wfc_real + 1j * wfc_im)
    wfc = wfc * wfc
    wfc = np.reshape(wfc,(xDim*yDim*zDim))
    maximum = max(wfc)
    wfc /= maximum
    wfc = np.reshape(wfc,(xDim,yDim,zDim))
    #print(wfc)
    return wfc

def wfc_phase(xDim, yDim, zDim, data_dir, pltval, i):
    print(i)
    data_real = "../" + data_dir + "/wfc_0_const_%s" % i
    data_im = "../" + data_dir + "/wfc_0_consti_%s" % i
    if (pltval == "wfc_ev"):
        data_real = "../" + data_dir + "/wfc_ev_%s" % i
        data_im = "../" + data_dir + "/wfc_evi_%s" % i
    elif (pltval == "wfc_ramp"):
        data_real = "../" + data_dir + "/wfc_0_ramp_%s" % i
        data_im = "../" + data_dir + "/wfc_0_rampi_%s" % i
    lines_real = np.loadtxt(data_real)
    lines_im = np.loadtxt(data_im)
    wfc_real = np.reshape(lines_real, (xDim,yDim, zDim));
    wfc_im = np.reshape(lines_im, (xDim,yDim, zDim));
    wfc = (wfc_real + 1j * wfc_im)
    wfc = np.angle(wfc)
    wfc = np.reshape(wfc,(xDim*yDim*zDim))
    maximum = max(wfc)
    minimum = min(wfc)
    for i in range(0,len(wfc)):
        wfc[i] = (wfc[i] - minimum) / (maximum - minimum)
    wfc = np.reshape(wfc,(xDim,yDim,zDim))
    return wfc

def var(xDim, yDim, zDim, data_dir, pltval):
    data = "../" + data_dir + "/" + pltval
    lines = np.loadtxt(data)
    maximum = max(lines)
    minimum = min(lines)
    for i in range(0,len(lines)):
        lines[i] = (lines[i] - minimum) / (maximum - minimum)
    val = np.reshape(lines, (xDim,yDim,zDim));
    return val

def proj_var2d(xdim, yDim, zDim, data_dir, pltval):
    filename = "../" + data_dir + "/" + "val"
    file = open(filename,"w")
    data = "../" + data_dir + "/" + pltval
    lines = np.loadtxt(data)
    var_data = np.reshape(lines, (xDim, yDim, zDim))
    for k in range(0,xDim):
        for j in range(0,yDim):
            file.write(str(var_data[k][j][zDim/2])+'\n')
    file.close


def proj_2d(xDim, yDim, zDim, data_dir, pltval, i):
    filename = "../" + data_dir + "/wfc_0"
    print(i)
    data_real = "../" + data_dir + "/wfc_0_const_%s" % i
    data_im = "../" + data_dir + "/wfc_0_consti_%s" % i
    if (pltval == "wfc_ev"):
        data_real = "../" + data_dir + "/wfc_ev_%s" % i
        data_im = "../" + data_dir + "/wfc_evi_%s" % i
    elif (pltval == "wfc_ramp"):
        data_real = "../" + data_dir + "/wfc_0_ramp_%s" % i
        data_im = "../" + data_dir + "/wfc_0_rampi_%s" % i
    lines_real = np.loadtxt(data_real)
    lines_im = np.loadtxt(data_im)
    print(len(lines_real))
    wfc_real = np.reshape(lines_real, (xDim,yDim,zDim));
    wfc_im = np.reshape(lines_im, (xDim,yDim, zDim));
    wfc = abs(wfc_real + 1j * wfc_im)
    wfc = wfc * wfc
    file = open(filename,'w')
    for k in range(0,xDim):
        for j in range(0,yDim):
            file.write(str(wfc[xDim/2][k][j]) + '\n')
    file.close()

def proj_k2d(xDim, yDim, zDim, data_dir, pltval, i):
    filename = "../" + data_dir + "/wfc_1"
    print(i)
    data_real = "../" + data_dir + "/wfc_0_const_%s" % i
    data_im = "../" + data_dir + "/wfc_0_consti_%s" % i
    lines_real = np.loadtxt(data_real)
    lines_im = np.loadtxt(data_im)
    print(len(lines_real))
    wfc_real = np.reshape(lines_real, (xDim,yDim,zDim));
    wfc_im = np.reshape(lines_im, (xDim,yDim, zDim));
    wfc = np.fft.fftshift(np.fft.fftn(wfc_real + 1j * wfc_im))
    wfc = abs(wfc) * abs(wfc)
    file = open(filename,'w')
    for k in range(0,xDim):
        for j in range(0,yDim):
            file.write(str(wfc[j][k][zDim/2]) + '\n')
    file.close()

# function to output the bvox bin data of a matrix
def to_bvox(item, xDim, yDim, zDim, nframes, filename):
    header = np.array([xDim, yDim, zDim, nframes])
    binfile = open(filename, "wb")
    header.astype('<i4').tofile(binfile)
    item.astype('<f4').tofile(binfile)
    binfile.close()

'''
proj_var2d(xDim, yDim, zDim, "data", "fieldz")
proj_2d(xDim, yDim, zDim,"data","wfc",50000)
#proj_2d(xDim, yDim, zDim,"data","wfc",1000000)
#proj_k2d(xDim, yDim, zDim,"data","wfc",500000)

item_wfc = wfc_density(xDim, yDim, zDim,"data","wfc",50000)
#item_wfc = wfc_density(xDim, yDim, zDim,"data","wfc",1000000)
item_phase = wfc_phase(xDim, yDim, zDim,"data","wfc",50000)
#item_phase = wfc_phase(xDim, yDim, zDim,"data","wfc",1000000)
item_var = var(xDim, yDim, zDim,"data","By_0")
item2_var = var(xDim, yDim, zDim,"data","Edges_0")

to_bvox(item_wfc, xDim, yDim, zDim, 1, "test_wfc.bvox")
to_bvox(item_phase, xDim, yDim, zDim, 1, "test_phase.bvox")
to_bvox(item_var, xDim, yDim, zDim, 1, "test_var.bvox")
to_bvox(item2_var, xDim, yDim, zDim, 1, "test_edges.bvox")
'''

'''
# Writing out the potential
item_pot = var(xDim, yDim, zDim, "data", "V_0")
to_bvox(item_pot, xDim, yDim, zDim, 1, "test_pot.bvox")
#item_gauge = var(xDim, yDim, zDim, "data", "Az_0")
#to_bvox(item_gauge, xDim, yDim, zDim, 1, "test_gauge.bvox")
for i in range(0,21):
    num = i * 5000
    item = wfc_density(xDim, yDim, zDim, "data", "wfc", num)
    to_bvox(item, xDim, yDim, zDim, 1, "wfc_%s.bvox" %num)

item_edges = var(xDim, yDim, zDim,"data","Edges_0")
to_bvox(item_edges, xDim, yDim, zDim, 1, "test_edges.bvox")
'''
'''

for i in range(0,21):
    num = i * 1
    print(num)
    item = var(xDim, yDim, zDim, "data", "Edges_%s"%num)
    to_bvox(item, xDim, yDim, zDim, 1, "EDGES_%s.bvox" %num)

'''
'''
proj_var2d(xDim, yDim, zDim, "data", "fieldz")
item = var(xDim, yDim, zDim, "data", "fieldz")
to_bvox(item, xDim, yDim, zDim, 1, "HE11check.bvox")
'''

'''
proj_2d(xDim, yDim, zDim, "data", "wfc_ramp", 100000)
#item_edges = var(xDim, yDim, zDim,"data","Edges_0")
#to_bvox(item_edges, xDim, yDim, zDim, 1, "test_edges.bvox")
'''

'''
print("start")
item_edges = var(xDim, yDim, zDim,"data","Edges_std")
to_bvox(item_edges, xDim, yDim, zDim, 1, "edges_std.bvox")
to_vtk(item_edges, xDim, yDim, zDim, 1, "edges_std.vtk")
print("starting linpol")
item_edges = var(xDim, yDim, zDim,"data","Edges_linpol")
to_bvox(item_edges, xDim, yDim, zDim, 1, "edges_linpol.bvox")
to_vtk(item_edges, xDim, yDim, zDim, 1, "edges_linpol.vtk")
'''

item = wfc_density(xDim, yDim, zDim, "data", "wfc", 100000)
to_vtk(item, xDim, yDim, zDim, 1, "wfc.vtk")
