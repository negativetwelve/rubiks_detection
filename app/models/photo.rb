class Photo < ActiveRecord::Base
  belongs_to :cube
  has_attached_file :image, :styles => { :medium => "300x300>", :thumb => "100x100>" }
  
  def color_distance(c, d)
    Math.sqrt((c[0]-d[0])**2 + (c[1]-d[1])**2 + (c[2]-d[2])**2)
  end
  
  def get_colors
    require 'rmagick'
    img =  Magick::Image.read(self.image.path).first
    #pix = img.scale(1, 1)
    values = []
    output = []
    colors = {'red' => [150, 80, 80],
              'blue' => [20, 20, 200],
              'green' => [46, 139, 87],
              'orange' => [160, 140, 160],
              'white' => [110, 130, 210],
              'yellow' => [120, 160, 100]}
    coordinates = [[210, 230, 130, 150], [310, 330, 130, 150], [410, 430, 130, 150], [210, 230, 230, 250], [310, 330, 230, 250], [410, 430, 230, 250], [210, 230, 330, 350], [310, 330, 330, 350], [410, 430, 330, 350]]
    coordinates.each do |c|
      red, blue, green = 0, 0, 0
      (c[0]..c[1]).each do |x|
        (c[2]..c[3]).each do |y|
          pixel = img.pixel_color(x, y)
          red += pixel.red
          blue += pixel.blue
          green += pixel.green
        end
      end
      value = Magick::Pixel.new(red/441, green/441, blue/441).to_color(Magick::SVGCompliance, false, 8, false)
      color = value[5..value.length-2].split(',')
      rgb = [color[0].to_i, color[1].to_i, color[2].to_i]
      output << rgb
      distance = 10000000000
      new_color = ""
      colors.each do |name, a|
        if color_distance(rgb, a) < distance
          new_color = name
          distance = color_distance(rgb, a)
        end
      end
      values << new_color
    end
#    (310..330).each do |x|
#      (230..250).each do |y|
#        pixel = img.pixel_color(x,y,"white")
#      end
#    end
#    img.write(self.image.path)
    [values, output]
  end


end
