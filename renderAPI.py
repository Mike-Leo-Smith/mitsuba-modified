from  mitsuba.core  import  *
from  mitsuba.render  import  SceneHandler
from  mitsuba.render  import  RenderQueue,  RenderJob
import multiprocessing
import numpy as np
import time
import pyexr
from os.path import expanduser
#  Get  a  reference  to  the  thread's  file  resolver
fileResolver  =  Thread.getThread().getFileResolver()
#  Register  any  searchs  path  needed  to  load  scene  resources  (optional)
#fileResolver.appendPath('<path  to  scene  directory>')
#  Optional:  supply  parameters  that  can  be  accessed
#  by  the  scene  (e.g.  as  $myParameter)
paramMap  =  StringMap()
paramMap['myParameter']  =  'value'
#  Load  the  scene  from  an  XML  file
scene  =  SceneHandler.loadScene(fileResolver.resolve(expanduser("/home/xhg/Desktop/kujiale_files/mitsuba/3FO4K2O1B9I5_full_new_diffuse_twosided.xml")),  paramMap)

scheduler  =  Scheduler.getInstance()
#  Start  up  the  scheduling  system  with  one  worker  per  local  core
for i in  range(0,  multiprocessing.cpu_count()):
    scheduler.registerWorker(LocalWorker(i,  'wrk%i'  %  i))

scheduler.start()
#  Create  a  queue  for  tracking  render  jobs
queue  =  RenderQueue()

sensor  =  scene.getSensor()

shapes = scene.getShapes()


# Pre Rendering for kd tree
scene.setDestinationFile('Fake')
job  =  RenderJob('fakeJob',  scene,  queue)
job.start()

queue.waitLeft(0)
queue.join()

aabb    =  scene.getAABB()
leftmins = []
rightmaxs = []


print "Nature AABB ##################"
print aabb.getCorner(0)
print aabb.getCorner(7)
print "##################"

#for Invalid Aabb

#Bound for L3D201S8ENDIAFHGSAUI5NFSLUF3P3XC888 1 rooms(OK)
# leftmins.append(Point(-6023, 1029, 0))
# rightmaxs.append(Point(-2422, 4829, 2800))

#Bound for 3FO4K2PV12YH 3 rooms(OK)
#leftmins.append(Point(-3054.82, -458.532, 0))
#rightmaxs.append(Point(352.464, 3350.23, 2800))

# leftmins.append(Point(-3054.82, -3120.85, 0))
# rightmaxs.append(Point(-1389.66, -578.532, 2800))

# leftmins.append(Point(1036.77, -2435.94, 0))
# rightmaxs.append(Point(2654.31, 4800, 2800))

#Bound for 3FO4K2O1B9I5 6 rooms(OK)
leftmins.append(Point(-5521, -5922.8, 0))
rightmaxs.append(Point(-202, -2651, 2800))

leftmins.append(Point(-5482, 2059, 0))
rightmaxs.append(Point(-702, 5378, 2800))

leftmins.append(Point(1858, 2059, 0))
rightmaxs.append(Point(5651, 5379, 2800))

leftmins.append(Point(1768, -4111, 0))
rightmaxs.append(Point(3418, -1361, 2800))

leftmins.append(Point(3618, -4111, 0))
rightmaxs.append(Point(5651, -1361, 2800))

leftmins.append(Point(-5483, -1211, 0))
rightmaxs.append(Point(5651, 1819, 2800))

#Bound for 3FO4K2PH3QVQ 4 rooms(OK)
# leftmins.append(Point(212, -2326.43, 0))
# rightmaxs.append(Point(3414.71, 418.567, 2700))

# leftmins.append(Point(-1370.29, -5256.43, 0))
# rightmaxs.append(Point(69.708, -2566.43, 2700))

# leftmins.append(Point(-4970.29, -2326.43, 0))
# rightmaxs.append(Point(99.79, 4273.57, 2700))

# leftmins.append(Point(-5950.49, 3123.57, 0))
# rightmaxs.append(Point(-3354.96, 6148.567, 2700))

#Bound for 3FO4K2PDTEIJ 5 rooms(OK)
# leftmins.append(Point(-11721.6, 2905.74, 0))
# rightmaxs.append(Point(-2551.58, 6205.74, 2800))

# leftmins.append(Point(-6231.58, -7995.74, 0))
# rightmaxs.append(Point(-2551.58, 10795.7, 2800))

# leftmins.append(Point(-10221.6, 7345.7, 0))
# rightmaxs.append(Point(-7571.58, 10795.7, 2800))

# leftmins.append(Point(-10221.6, 10915.7, 0))
# rightmaxs.append(Point(-8071.58, 14282.7, 2800))

# leftmins.append(Point(-6231.58, 10915.7, 0))
# rightmaxs.append(Point(-2551.58, 14295.7, 2800))

#Bound for 3FO4K2P802EF 7 rooms(OK)
# leftmins.append(Point(-6790, -5600, 0))
# rightmaxs.append(Point(-2800, 3429, 2800))

# leftmins.append(Point(-5560, 3429, 0))
# rightmaxs.append(Point(-1400, 6429, 2800))

# leftmins.append(Point(-2800.12, 1019.5, 0))
# rightmaxs.append(Point(-1250, 3429.5, 2800))

# leftmins.append(Point(-1110, 1019.5, 0))
# rightmaxs.append(Point(2419.88, 3429.5, 2800))

# leftmins.append(Point(-2800.12, -4560, 0))
# rightmaxs.append(Point(-90, -440.493, 2800))

# leftmins.append(Point(49.88, -4590.5, 0))
# rightmaxs.append(Point(2919.88, -440.493, 2800))

# leftmins.append(Point(3059.88, -5590.49, 0))
# rightmaxs.append(Point(6339.88, 819, 2800))


#Bound for 3FO4K2PSOO65 6 rooms(OK)
# leftmins.append(Point(-5254.98, -3329.11, 0))
# rightmaxs.append(Point(-1912.3, -1829.11, 2800))

# leftmins.append(Point(-2792.32, -1589.11, 0))
# rightmaxs.append(Point(-5254.98, 130.888, 2800))

# leftmins.append(Point(-1932.3, 370.889, 0))
# rightmaxs.append(Point(-5254.98, 3096.67, 2800))

# leftmins.append(Point(-1812.3, -3093.33, 0))
# rightmaxs.append(Point(3907.68, 130.288, 2800))

# leftmins.append(Point(685, 370, 0))
# rightmaxs.append(Point(4148, 3096, 2800))

# leftmins.append(Point(-1812, 1390, 0))
# rightmaxs.append(Point(565, 3096, 2800))


#Bound for 3FO4K2PT3MCB 5 rooms(OK)
# leftmins.append(Point(-6612, -4755, 0))
# rightmaxs.append(Point(-3260, -75, 2800))

# leftmins.append(Point(1230, -4755, 0))
# rightmaxs.append(Point(4834, -75, 2800))

# leftmins.append(Point(-3140, -4755, 0))
# rightmaxs.append(Point(1110, 4268, 2800))

# leftmins.append(Point(1230, 1998, 0))
# rightmaxs.append(Point(4834, 5356, 2800))

# leftmins.append(Point(-4420, 4268, 0))
# rightmaxs.append(Point(-1974, 6442, 2800))

#Bound for 3FO4K2PYHHRS 11 rooms(OK)
# leftmins.append(Point(-9570, -3720, 0))
# rightmaxs.append(Point(-6270, 3630, 2800))

# leftmins.append(Point(-4949, -2540, 0))
# rightmaxs.append(Point(-3190, -1170, 2800))

# leftmins.append(Point(-4832, -4320, 0))
# rightmaxs.append(Point(-3379, -2750, 2800))

# leftmins.append(Point(-6069, 340, 0))
# rightmaxs.append(Point(-3309, 3630, 2800))

# leftmins.append(Point(-3208, -1050, 0))
# rightmaxs.append(Point(-119, 3630, 2800))

# leftmins.append(Point(120, 340, 0))
# rightmaxs.append(Point(3210, 3630, 2800))

# leftmins.append(Point(120, -2539, 0))
# rightmaxs.append(Point(2125, 100, 2800))

# leftmins.append(Point(1890, -2540, 0))
# rightmaxs.append(Point(4952, -1162, 2800))

# leftmins.append(Point(3370, 340, 0))
# rightmaxs.append(Point(6070, 3630, 2800))

# leftmins.append(Point(3380, -4320, 0))
# rightmaxs.append(Point(6170, -2750, 2800))

# leftmins.append(Point(6270, -3719, 0))
# rightmaxs.append(Point(9570, 3630, 2800))

#Bound for 3FO4K2VXB3TL 8 rooms(OK)
# leftmins.append(Point(-9459, 423, 7052))
# rightmaxs.append(Point(-2514, 5694, 10352))

# leftmins.append(Point(-5876, -4838, 7052))
# rightmaxs.append(Point(-3344, 182.7, 10352))

# leftmins.append(Point(-9699, -4948, 3751))
# rightmaxs.append(Point(-6116, -1354, 7051))

# leftmins.append(Point(-5875, -5711, 3751))
# rightmaxs.append(Point(148, 482, 7051))

# leftmins.append(Point(-6116, -5711, 0))
# rightmaxs.append(Point(148, 303, 3750))

# leftmins.append(Point(-9699, 243, 0))
# rightmaxs.append(Point(-7293, 2596, 3750))

# leftmins.append(Point(-6116, 423, 0))
# rightmaxs.append(Point(-2514, 5934, 3750))

# leftmins.append(Point(-2274, 302, 0))
# rightmaxs.append(Point(149, 5694, 3750))

# Bound for 3FO4K6JA2DRR 7 rooms(OK)
# leftmins.append(Point(-5462, -178, 0))
# rightmaxs.append(Point(-3432, 2378.5, 2800))

# leftmins.append(Point(-3208.68, -5053.53, 0))
# rightmaxs.append(Point(934.902, 3472.24, 2800))

# leftmins.append(Point(1034.43, -283.305, 0))
# rightmaxs.append(Point(3854.39, 3472.24, 2800))

# leftmins.append(Point(1027.85, -4500, 0))
# rightmaxs.append(Point(2615.8, -1614.22, 2800))

# leftmins.append(Point(2761, -5106, 0))
# rightmaxs.append(Point(5396, -1614, 2800))

# leftmins.append(Point(5541, -5106, 0))
# rightmaxs.append(Point(7623, -2905, 2800))

# leftmins.append(Point(4012, -1469, 0))
# rightmaxs.append(Point(7623, 3322, 2800))

# Bound for 3FO4K2OWMS73 4 rooms(OK)
# leftmins.append(Point(2443.34, -1306.9, 0))
# rightmaxs.append(Point(5999, 2719, 2800))

# leftmins.append(Point(1168, -4768, 0))
# rightmaxs.append(Point(4134, -1506, 2800))

# leftmins.append(Point(-1984, -4746, 0))
# rightmaxs.append(Point(968, -490, 2800))

# leftmins.append(Point(-3918.2, -1307, 0))
# rightmaxs.append(Point(2243, 3379, 2800))

# Bound for 3FO4K2ONCBAQ 5 rooms (until now 72 rooms)
# leftmins.append(Point(-675.3, 1282, 0))
# rightmaxs.append(Point(4194.8, 7802, 2900))

# leftmins.append(Point(964.7, -458, 0))
# rightmaxs.append(Point(4194.8, 1102, 2900))

# leftmins.append(Point(-3459.3, -585.3, 0))
# rightmaxs.append(Point(-1315.25, 1162, 2900))

# leftmins.append(Point(-4765.3, -4858, 0))
# rightmaxs.append(Point(-1315.25, -705.3, 2900))

# leftmins.append(Point(1834.8, -4858, 0))
# rightmaxs.append(Point(5094.8, -698, 2900))

# Bound for 3FO4K2OINA7O 7 rooms
# leftmins.append(Point(-5703, -4983.8, 0))
# rightmaxs.append(Point(-1889.61, -1168, 2800))

# leftmins.append(Point(2554.9, -5188, 0))
# rightmaxs.append(Point(5705, -2395, 2800))

# leftmins.append(Point(-5703, -1049, 0))
# rightmaxs.append(Point(-3100, 769.5, 2800))

# leftmins.append(Point(-5703, 973, 0))
# rightmaxs.append(Point(-3100, 2782, 2800))

# leftmins.append(Point(-4803, 2892.2, 0))
# rightmaxs.append(Point(-1485.7, 6416, 2800))

# leftmins.append(Point(2364.8, 2588, 0))
# rightmaxs.append(Point(4330, 5000, 2800))

# leftmins.append(Point(-1280.8, -4383.8, 0))
# rightmaxs.append(Point(2254.9, 5306.5, 2800))

# Bound for 3FO4K2OI434X 14 rooms
# leftmins.append(Point(-7550.9, -5289.6, 3100))
# rightmaxs.append(Point(6848.26, -853.6, 6000))

# leftmins.append(Point(-7550.9, -5289.6, 0))
# rightmaxs.append(Point(6848.26, -853.6, 3100))

# leftmins.append(Point(-6401.5, 1615, 3100))
# rightmaxs.append(Point(-3723, 6060, 6000))

# leftmins.append(Point(-3139.9, 3079.3, 3100))
# rightmaxs.append(Point(-1756.2, 4899.3, 6000))

# leftmins.append(Point(-3603, -613, 3100))
# rightmaxs.append(Point(-1556.04, 2959.3, 6000))

# leftmins.append(Point(969.6, -613.6, 3100))
# rightmaxs.append(Point(2824.2, 2959.3, 6000))

# leftmins.append(Point(968.6, 2959.3, 3100))
# rightmaxs.append(Point(2824.2, 4895.9, 6000))

# leftmins.append(Point(2944.2, 1495, 3100))
# rightmaxs.append(Point(5598.8, 6060, 6000))

# leftmins.append(Point(-6401.5, 1615, 0))
# rightmaxs.append(Point(-3723, 6060, 3100))

# leftmins.append(Point(-3139.9, 3079.3, 000))
# rightmaxs.append(Point(-1756.2, 4899.3, 3100))

# leftmins.append(Point(-3603, -613, 0))
# rightmaxs.append(Point(-1556.04, 2959.3, 3100))

# leftmins.append(Point(969.6, -613.6, 0))
# rightmaxs.append(Point(2824.2, 2959.3, 3100))

# leftmins.append(Point(968.6, 2959.3, 0))
# rightmaxs.append(Point(2824.2, 4895.9, 3100))

# leftmins.append(Point(2944.2, 1495, 0))
# rightmaxs.append(Point(5598.8, 6060, 3100))

step = 0.5
framesNum = 0
np.random.seed(int(time.time()))

sampler = sensor.getSampler()
originSampler = sampler.clone()

testprop = sampler.getProperties()
testprop['sampleCount'] = 16
pmgr  =  PluginManager.getInstance()
testsampler  =  pmgr.createObject(testprop)
testsampler.configure()

for i in range(100000):
    for shape in shapes:
        if shape.getName() == "final":
            for index in range(100000000):
                item = shape.getElement(index)
                if item is None:
                    break
                
                bsdf = item.getBSDF()
                prop = bsdf.getProperties()

                if prop.getPluginName() == "twosided":
                    pmgr  =  PluginManager.getInstance()
                    newbsdf  =  pmgr.createObject(bsdf.getProperties())
                    
                    bsdfprops = Properties('diffuse')
                    spectrum  = Spectrum(1.0)
                    spectrum.fromLinearRGB(np.random.rand(1)[0], np.random.rand(1)[0], np.random.rand(1)[0])
                    bsdfprops['reflectance'] = spectrum
                    singlebsdf = pmgr.createObject(bsdfprops)
                    singlebsdf.configure()
                    newbsdf.addChild(singlebsdf)
                    newbsdf.configure()

                    item.setBSDF(newbsdf)

    AabbChoice = np.random.randint(len(rightmaxs), size=1)[0]
    leftmin = leftmins[AabbChoice]
    rightmax = rightmaxs[AabbChoice]
    extend = rightmax - leftmin

    origin = Point(extend[0] * (0.25 + 0.5 * np.random.rand(1)[0]) + leftmin[0], extend[1] * (0.25 + 0.5 * np.random.rand(1)[0]) + leftmin[1], extend[2] * (0.25 + 0.5 * np.random.rand(1)[0]) + leftmin[2])
    target = Point(extend[0] * np.random.rand(1)[0] + leftmin[0], extend[1] * np.random.rand(1)[0] + leftmin[1], extend[2] * np.random.rand(1)[0] + leftmin[2])

    np_orgin = np.array([origin[0], origin[1], origin[2]])
    np_target = np.array([target[0], target[1], target[2]])

    np_dir = (np_target - np_orgin) / np.linalg.norm(np_target - np_orgin)
    np_cross = np.array([0, 0, 0])
    np_cross[np.argmax(np_dir)] = 1
    np_trans = np.cross(np_dir, np_cross)

    #rotationCur = Transform.translate(Vector(np_trans[0], np_trans[1], np_trans[2]) * step)

    # for frame j and its neighbour
    for j in range(2):
        rotationCur = Transform.rotate(Vector(0,  1,  0),  0)
        if j == 1:
            randseed = np.random.randint(4, size=1)[0]
            if randseed == 0:
                rotationCur = Transform.rotate(Vector(0,  1,  0),  step)
            elif randseed == 1:
                rotationCur = Transform.rotate(Vector(0,  1,  0),  -step)
            elif randseed == 2:
                rotationCur = Transform.rotate(Vector(1,  0,  0),  step)
            elif randseed == 3:
                rotationCur = Transform.rotate(Vector(1,  0,  0),  -step)

        lookat = Transform.lookAt(rotationCur * origin, target,  rotationCur  * Vector(0.0, 0.0, 1))
        sensor.setWorldTransform(lookat)

        if j == 0:            
            sensor.setSampler(testsampler)
            sensor.configure()
            scene.configure()

            scene.setDestinationFile("Pre")
            job  =  RenderJob('Pre',  scene,  queue)
            job.start()

            queue.waitLeft(0)
            queue.join()

            sensor.setSampler(originSampler)
            sensor.configure()
            scene.configure()

            preResult = pyexr.open('Pre.exr').get('diffuse_dir')
            if np.count_nonzero(preResult > 0.005) < 384 * 512 * 0.3 or np.isnan(np.sum(preResult)):
                break

            framesNum = framesNum + 1



        if j == 0:
            scene.setDestinationFile("result/" + str(framesNum).zfill(10))
        elif j == 1:
            scene.setDestinationFile("result/" + str(framesNum).zfill(10) + "a")
        #  Create  a  render  job  and  insert  it  into  the  queue
        job  =  RenderJob('myRenderJob' + str(framesNum),  scene,  queue)
        job.start()

        queue.waitLeft(0)
        queue.join()
