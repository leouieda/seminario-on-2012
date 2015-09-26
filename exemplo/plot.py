import sys
import os
import numpy as np
import fatiando as ft

data = np.loadtxt(sys.argv[1], unpack=True)

lon, lat = data[0:2]
tensor = data[3:]
area = (lon.min(), lon.max(), lat.min(), lat.max())
bm = ft.vis.basemap(area, 'ortho')
shape = (100, 100)
titles = ['gxx', 'gxy', 'gxz', 'gyy', 'gyz', 'gzz']
ft.vis.figure(figsize=(12,7))
ft.vis.subplots_adjust(left=0.05, right=0.98, top=0.98, bottom=0.02,
    wspace=0.05, hspace=0.02)
for i in xrange(6):
    ft.vis.subplot(2, 3, i + 1)
    ft.vis.title(titles[i])
    bm.bluemarble()
    ft.vis.contourf(lon, lat, tensor[i], shape, 80, basemap=bm)
    ft.vis.colorbar(shrink=0.75)
    #ft.vis.draw_geolines(area, 15, 15, bm)
    #ft.vis.draw_coastlines(bm)
    #bm.drawmapboundary()
ft.vis.savefig('%s.png' % (os.path.splitext(sys.argv[1])[0]))
ft.vis.show()
