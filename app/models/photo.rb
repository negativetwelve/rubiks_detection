class Photo < ActiveRecord::Base
  has_attached_file :image, :styles => { :medium => "300x300>", :thumb => "100x100>" }
  
  def get_side
    require 'rmagick'
    img =  Magick::Image.read(self.image.path).first
    pix = img.scale(1, 1)
    averageColor = pix.pixel_color(100,100)
  end


end
