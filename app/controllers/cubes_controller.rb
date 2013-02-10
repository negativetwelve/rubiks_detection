class CubesController < ApplicationController
  Rails.application.routes.url_helpers
  
  def new
  end
  
  def create
    @cube = Cube.new(params[:cube])
    @cube.save
    redirect_to new_photo_path(cube_id: @cube.id)
  end
  
  def show
  end
end
