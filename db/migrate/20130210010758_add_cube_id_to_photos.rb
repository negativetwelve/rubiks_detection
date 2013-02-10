class AddCubeIdToPhotos < ActiveRecord::Migration
  def change
    add_index :photos, [:cube_id, :created_at]
  end
end
