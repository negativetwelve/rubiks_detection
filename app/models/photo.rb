class Photo < ActiveRecord::Base
  belongs_to :cube
  has_attached_file :image, :styles => { :medium => "300x300>", :thumb => "100x100>" }
  
  def get_colors
    require 'rmagick'
    img =  Magick::Image.read(self.image.path).first
    #pix = img.scale(1, 1)
    color = []
    red, blue, green = 0, 0, 0
    values = []
    img.each_pixel do |pixel, c, r|
      color << pixel
    end
    (280..300).each do |x|
      (200..220).each do |y|
        pixel = img.pixel_color(x, y)
        red += pixel.red
        blue += pixel.blue
        green += pixel.green
      end
    end
    values << Magick::Pixel.new(red/400, blue/400, green/400).to_color(Magick::X11Compliance, false, 8, false)
    red, blue, green = 0, 0, 0
    (180..200).each do |x|
      (100..120).each do |y|
        pixel = img.pixel_color(x, y)
        red += pixel.red
        blue += pixel.blue
        green += pixel.green
      end
    end
    values << Magick::Pixel.new(red/400, blue/400, green/400).to_color(Magick::X11Compliance, false, 8, false)
    
    return values
  end


end
