class Photo < ActiveRecord::Base
  belongs_to :cube
  has_attached_file :image, :styles => { :medium => "300x300>", :thumb => "100x100>" }
  
  def get_side
    require 'rmagick'
    img =  Magick::Image.read(self.image.path).first
    #pix = img.scale(1, 1)
    #averageColor = pix.pixel_color(0,0)
  end


end
